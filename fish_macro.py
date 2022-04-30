import win32com.client
import pyautogui
import cv2
import time
import random
import numpy as np

# create instance for sending keystroke to windows
shell = win32com.client.Dispatch("WScript.Shell")

# imagesearch source = github : https://github.com/drov0/python-imagesearch

# replace this with your own fish caught image if detection is off
image = 'fishcaught.png'
template = cv2.imread(image, 0)
template.shape[::-1]

start_x, start_y = pyautogui.size()


def imagesearch(precision=0.7):
    # tested on 1920 x 1080, increase/adjust offsets if failing
    im = pyautogui.screenshot(region=(start_x/2-50, start_y/2-100, 100, 100))
    # im.save(r'R:\testarea{}.png'.format(time.time())) #usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        # print("not found", max_val)
        return None
    # print(min_val, max_val, min_loc, max_loc)
    return max_loc


# 1 fish per about 23 sec. fishing rod 100 = 37 min. If you miss fish, it takes 33 sec to cast again.
# https://medium.com/@martin.lees/image-recognition-for-automation-with-python-711ac617b4e5
print("[FYI #1] 100 fishing rods = about 37 minutes OR 157 fishing rods = about 1 hour")
print(" ")
print("[FYI #2] ctrl + c <- exit the program")
print(" ")
print("Running...")
print("Made by silvernine, LegitPandas")

caught_fish = 0
total_tries = 0
consecutive_failed_tries = 0
timeout_start_fishing = time.time()

# 34 seconds timeout for failed detection case.
timeout = 34
while(True):
    # starting time
    timeout_start = time.time()

    # Initial value to keep the while loop started
    pos_fish = None

    # while fish is not caught yet or under specified timeout, keep looking for the ! sign
    while (pos_fish == None) and (time.time() < (timeout_start+timeout)):
        pos_fish = imagesearch()
        time.sleep(.5)

    if (pos_fish == None):
        consecutive_failed_tries += 1
        for i in range(0,2):
            print('\a')
            time.sleep(0.2)

    else:
        consecutive_failed_tries = 0

    if (consecutive_failed_tries > 2):
        print('Stopped due to too many failures')
        break

    # Send 'e' keystroke when fish is caught OR recast the bait if detection failed and timed out
    shell.SendKeys("e")

    # Recast the bait if detection was successful. Won't send 'e' if detection failed.
    if (time.time()-timeout_start) < timeout:
        time.sleep(5)  # time it takes to re-cast after pulling the bait out
        time.sleep(random.randint(15, 20)/10)  # add 1~2 sec random time
        shell.SendKeys("e")
        time.sleep(7)
        caught_fish += 1

    total_tries += 1
    print("You caught {} fish out of {} tries. Success rate is {}%.".format(int(caught_fish), int(
        total_tries), round(int(caught_fish)/int(total_tries)*100)))
