import pyautogui
import time
import random
import keyboard
while True:
    x=0
    y=0
    try:
        x, y = pyautogui.locateCenterOnScreen('1.png')
    except:
        print("An exception occurred")
    try:
        if x==0:
            x, y = pyautogui.locateCenterOnScreen('2.png')
    except:
        print("An exception occurred")
    try:
        if x==0:
            x, y = pyautogui.locateCenterOnScreen('3.png')
    except:
        print("An exception occurred")
    try:
        if x==0:
            x, y = pyautogui.locateCenterOnScreen('4.png')
    except:
        print("An exception occurred")
    if x!=0:
        print(x)
        print(y)
        pyautogui.click(x, y)
        time.sleep(random.randint(3, 5))
    if keyboard.is_pressed("esc"):
        print("esc pressed, ending loop")
        break
