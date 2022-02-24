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
faza=0;
numer=1;
ile_jedynek=0;
ile_dwojek=0;
ile_trojek=0;
ile_czworek=0;
ile_piatek=0;
ile_szostek=0;
ile_siodemek=0;
ile_osemek=0;
ile_dziewiatek=0;
ile_zer=0;
wyniki01=0
wyniki02=0
wyniki03=0
wyniki04=0
wyniki11=0
wyniki12=0
wyniki13=0
wyniki14=0
wyniki21=0
wyniki22=0
wyniki23=0
wyniki24=0
wyniki31=0
wyniki32=0
wyniki33=0
wyniki34=0
zmiany=False
tablica=[]
czas=0.7
ilosc_powtorzen=1


time.sleep(10)
def poczatek():
    pyautogui.click(950, 310)
    time.sleep(czas)
    pyautogui.click(950, 670)
    time.sleep(czas)
    pyautogui.click(750, 670)
    pyautogui.click(750, 670)
def funkcja(i):
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    pyautogui.click(850, 670)
    time.sleep(czas)
    pyautogui.click(650, 650)
    pyautogui.click(650, 650)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    if Tk().clipboard_get()=="Gratulacje":
        print(".Ukonczone")
        end = time.time()
        print(end - start)
        tablica.clear()
        faza=0
    else:
        time.sleep(czas)
        pyautogui.click(850, 770)
        pyautogui.click(850, 770)
        pyautogui.click(850, 770)
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')

        if Tk().clipboard_get().find('0')!=-1:
            print("Znalezione"+str(i))
    pyautogui.click(850, 570)
    time.sleep(czas)
    return zmiany
for i in range(ilosc_powtorzen):
    wyniki01=0
    wyniki02=0
    wyniki03=0
    wyniki04=0
    wyniki11=0
    wyniki12=0
    wyniki13=0
    wyniki14=0
    wyniki21=0
    wyniki22=0
    wyniki23=0
    wyniki24=0
    wyniki31=0
    wyniki32=0
    wyniki33=0
    wyniki34=0
    start = time.time()
    ile_jedynek=0
    ile_dwojek=0
    ile_trojek=0
    ile_czworek=0
    ile_piatek=0
    ile_szostek=0
    ile_siodemek=0
    ile_osemek=0
    ile_dziewiatek=0
    ile_zer=0
    tablica.clear()
    numer=1
    if faza==0:
        for i in range(10):
            if len(tablica)<4:
                pyautogui.click(950, 310)
                r = None
                while r is None:
                    r = pyautogui.locateOnScreen('1.png')
                pyautogui.click(950, 670)
                r = None
                while r is None:
                    r = pyautogui.locateOnScreen('2.png')
                pyautogui.click(750, 670)
                pyautogui.click(750, 670)
                if numer==1:
                    pyperclip.copy("1111")
                if numer==2:
                    pyperclip.copy("2222")
                if numer==3:
                    pyperclip.copy("3333")
                if numer==4:
                    pyperclip.copy("4444")
                if numer==5:
                    pyperclip.copy("5555")
                if numer==6:
                    pyperclip.copy("6666")
                if numer==7:
                    pyperclip.copy("7777")
                if numer==8:
                    pyperclip.copy("8888")
                if numer==9:
                    pyperclip.copy("9999")
                if numer==10:
                    pyperclip.copy("1000")

                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('ctrl')
                pyautogui.click(850, 670)
                r = None
                while r is None:
                    r = pyautogui.locateOnScreen('3.png')
                pyautogui.click(850, 770)
                pyautogui.click(850, 770)
                pyautogui.click(850, 770)
                pyautogui.keyDown('ctrl')
                pyautogui.press('c')
                pyautogui.keyUp('ctrl')
                if numer==1:
                    ile_jedynek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_jedynek)):
                        tablica.append("1")
                if numer==2:
                    ile_dwojek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_dwojek)):
                        tablica.append("2")
                if numer==3:
                    ile_trojek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_trojek)):
                        tablica.append("3")
                if numer==4:
                    ile_czworek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_czworek)):
                        tablica.append("4")
                if numer==5:
                    ile_piatek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_piatek)):
                        tablica.append("5")
                if numer==6:
                    ile_szostek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_szostek)):
                        tablica.append("6")
                if numer==7:
                    ile_siodemek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_siodemek)):
                        tablica.append("7")
                if numer==8:
                    ile_osemek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_osemek)):
                        tablica.append("8")
                if numer==9:
                    ile_dziewiatek=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_dziewiatek)):
                        tablica.append("9")
                if numer==10:
                    ile_zer=Tk().clipboard_get().split(": ")[1].split("\n")[0]
                    for i in range(int(ile_zer)):
                        tablica.append("0")
                numer=numer+1
                pyautogui.click(850, 570)
                r = None
                while r is None:
                    r = pyautogui.locateOnScreen('4.png')

        print(str(ile_jedynek)+" "+str(ile_dwojek)+" "+str(ile_trojek)+" "+str(ile_czworek)+" "+str(ile_piatek)+" "+str(ile_szostek)+" "+str(ile_siodemek)+" "+str(ile_osemek)+" "+str(ile_dziewiatek)+" "+str(ile_zer)) 
        print(tablica)
        end = time.time()
        print(end - start)
        faza=1
    for i in range(24):
        if faza==1:
            pyautogui.click(950, 310)
            r = None
            while r is None:
                r = pyautogui.locateOnScreen('1.png')
            pyautogui.click(950, 670)
            r = None
            while r is None:
                r = pyautogui.locateOnScreen('2.png')
            pyautogui.click(750, 670)
            pyautogui.click(750, 670)
            if i==0:
                pyperclip.copy(tablica[0]+tablica[1]+tablica[2]+tablica[3])
            if i==1:
                pyperclip.copy(tablica[0]+tablica[1]+tablica[3]+tablica[2])
            if i==2:
                pyperclip.copy(tablica[0]+tablica[2]+tablica[1]+tablica[3])
            if i==3:
                pyperclip.copy(tablica[0]+tablica[2]+tablica[3]+tablica[1])
            if i==4:
                pyperclip.copy(tablica[0]+tablica[3]+tablica[2]+tablica[1])
            if i==5:
                pyperclip.copy(tablica[0]+tablica[3]+tablica[1]+tablica[2])
            if i==6:
                pyperclip.copy(tablica[1]+tablica[0]+tablica[2]+tablica[3])
            if i==7:
                pyperclip.copy(tablica[1]+tablica[0]+tablica[3]+tablica[2])
            if i==8:
                pyperclip.copy(tablica[1]+tablica[2]+tablica[0]+tablica[3])
            if i==9:
                pyperclip.copy(tablica[1]+tablica[2]+tablica[3]+tablica[0])
            if i==10:
                pyperclip.copy(tablica[1]+tablica[3]+tablica[2]+tablica[0])
            if i==11:
                pyperclip.copy(tablica[1]+tablica[3]+tablica[0]+tablica[2])
            if i==12:
                pyperclip.copy(tablica[2]+tablica[1]+tablica[0]+tablica[3])
            if i==13:
                pyperclip.copy(tablica[2]+tablica[1]+tablica[3]+tablica[0])
            if i==14:
                pyperclip.copy(tablica[2]+tablica[3]+tablica[1]+tablica[0])
            if i==15:
                pyperclip.copy(tablica[2]+tablica[3]+tablica[0]+tablica[1])
            if i==16:
                pyperclip.copy(tablica[2]+tablica[0]+tablica[1]+tablica[3])
            if i==17:
                pyperclip.copy(tablica[2]+tablica[0]+tablica[3]+tablica[1])
            if i==18:
                pyperclip.copy(tablica[3]+tablica[1]+tablica[2]+tablica[0])
            if i==19:
                pyperclip.copy(tablica[3]+tablica[1]+tablica[0]+tablica[2])
            if i==20:
                pyperclip.copy(tablica[3]+tablica[2]+tablica[1]+tablica[0])
            if i==21:
                pyperclip.copy(tablica[3]+tablica[2]+tablica[0]+tablica[1])
            if i==22:
                pyperclip.copy(tablica[3]+tablica[0]+tablica[1]+tablica[2])
            if i==23:
                pyperclip.copy(tablica[3]+tablica[0]+tablica[2]+tablica[1])
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            pyautogui.click(850, 670)
            time.sleep(czas)
            pyautogui.click(650, 650)
            pyautogui.click(650, 650)
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            if Tk().clipboard_get()=="Gratulacje":
                print(".Ukonczone")
                end = time.time()
                print(end - start)
                tablica.clear()
                faza=0
            pyautogui.click(850, 570)
            r = None
            while r is None:
                r = pyautogui.locateOnScreen('4.png')

    else:
        faza=0
            
           