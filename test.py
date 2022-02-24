import pyautogui
icon_to_click = "Recycle Bin"

r = None
while r is None:
    r = pyautogui.locateOnScreen('dddd.png')
print(icon_to_click + ' now loaded'+str(r))