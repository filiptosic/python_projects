import selenium
import pyautogui
from time import sleep as sleep
while True:
    pyautogui.moveTo(100, 200)
    sleep(3)
    pyautogui.moveTo(400, 200)
    sleep(3)
    pyautogui.moveTo(300, 200)
    sleep(3)
    pyautogui.moveTo(400, 200)
    pyautogui.typewrite('I\'m awake \n')