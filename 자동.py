import pyautogui
import time

import keyboard

while True:
    if keyboard.read_key() == "shift":
        time.sleep(0.2)
        print('backspace')
        pyautogui.press('backspace')
        pyautogui.press('tab')
        print('tab')
        pyautogui.press('down')
        print('down')       