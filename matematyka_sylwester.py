rozbijanie=""
znak=""
rozbijanie2=""
wynik=0
import pyautogui
import time
import random
import keyboard
from tkinter import Tk
import pyperclip
x=0
y=0


#787
#450

#790
#476
#3 razy kliknąć, skopiować, obliczyć 2 razy wrzucić
#977
#475

#while True:
for i in range(50):
    try:
        
        pyautogui.click(787, 450)
        pyautogui.click(787, 450)
        pyautogui.click(787, 450)
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        dzialanie = Tk().clipboard_get()
        if '+' in dzialanie:
            rozbijanie=dzialanie.split('+', 1 )
            znak="+"
            rozbijanie2=rozbijanie[1].split('=...',1)
        elif '-' in dzialanie:
            rozbijanie=dzialanie.split('-', 1 )
            znak="-"
            rozbijanie2=rozbijanie[1].split('=...',1)
        elif ':' in dzialanie:
            rozbijanie=dzialanie.split(':', 1 )
            znak=":"
            rozbijanie2=rozbijanie[1].split('=...',1)
        elif '*' in dzialanie:
            rozbijanie=dzialanie.split('*', 1 )
            znak="*"
            rozbijanie2=rozbijanie[1].split('=...',1)
        if znak=="+":
            wynik=int(rozbijanie[0])+int(rozbijanie2[0])
        elif znak=="-":
            wynik=int(rozbijanie[0])-int(rozbijanie2[0])
        elif znak=="*":
            wynik=int(rozbijanie[0])*int(rozbijanie2[0])
        elif znak==":":
            wynik=int(rozbijanie[0])/int(rozbijanie2[0])
        print("Wynik: " + str(wynik).split('.', 1 )[0])
        pyperclip.copy(str(wynik).split('.', 1 )[0])
        pyautogui.click(790, 476)
        pyautogui.click(790, 476)
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        pyautogui.click(977, 475)
        time.sleep(1) 
    except:
        print("An exception occurred")

#10+98=...
#10-98=...
#10:98=...
#10*98=...
