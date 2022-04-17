# Lost Ark Fish Macro
Automate fishing task in a game called Lost Ark using image detection.
This was a quick implementation of machine learning in gaming for fun :)

## Prerequisites
Python 3  
pyautogui  
cv2  
numpy

## Instruction
1. Install libraries mentioned in "Prerequisites" section.  
2. Place "fishcaught.png" in the same directory as the script.  
3. Run "fish_macro.py" script.  
4. Place your character in Lost Ark game near fishing location. Cast a fishing rod by clicking w.  
5. You are all set!  

## How it works
This script knows to pull the fishing rod out when the fish is caught by detecting the yellow exclamation mark.  
It waits until your character is ready, and casts another fishing rod.

## Troubleshooting
Depending on your screen/game's resolution, image provided might not match actual exclamation mark for you.
Simply take a screenshot and replace provided image with your own.

## Contributions
Thanks to drov0's python-imagesearch : https://github.com/drov0/python-imagesearch
