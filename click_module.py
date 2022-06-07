import pyautogui
import time
import sys
import datetime
import cv2

# testㅠ 
def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None : 
        # target = pyautogui.locateOnScreen(img_file)
        target = pyautogui.locateOnScreen(img_file, confidence = 0.915, grayscale = True)
        # target = pyautogui.locateOnScreen(img_file, confidence = 0.99)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_search(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target :
        return "searched"
    else : 
        return "nosearched" 
        # msg = f"[timeout {timeout}s] Target not found ({img_file}). Terminate program."
        # print(msg)
        # sys.exit()

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target :
        pyautogui.click(target)
        return "clicked"
    else : 
        return "noclicked" 
        # msg = f"[timeout {timeout}s] Target not found ({img_file}). Terminate program."
        # print(msg)
        # sys.exit()

def my_Move_click(img_file, timeout = 30, x=0, y=0):
    targetR100 = find_target(img_file, timeout)
    if targetR100 :
        pyautogui.moveTo(targetR100)
        pyautogui.move(x,y)
        pyautogui.click()
        return 1
    else : 
        return 2
        # msg = f"[timeout {timeout}s] Target not found ({img_file}). Terminate program."
        # print(msg)
        # sys.exit()  
        
    







