import pyautogui
import time
import keyboard

while True:
    print('waiting F6...')
    if keyboard.is_pressed('F6'):
        while True:
            time.sleep(0.01)
            pyautogui.press('left')
            print('left')
            time.sleep(0.01)
            pyautogui.press('right')
            print('right')
            print('\n')
            pyautogui.leftClick(806, 445)
            pyautogui.press('enter')
            print('click+enter')
            print('\n')
            time.sleep(0.01)
            pyautogui.press('left')
            print('left')
            time.sleep(0.01)
            pyautogui.press('right')
            print('right')
            print('\n')
            if keyboard.is_pressed('F7'):    
                break