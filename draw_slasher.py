import pyautogui
import keyboard

while True:
    print('waiting F6...')
    if keyboard.is_pressed('F6'):
        while True:
            # Loop 1
            pyautogui.leftClick(x=164, y=314)
            print('leftClick')
            pyautogui.dragTo(2100,314, 0.2)
            print('dragRight')
            print('\n')
            pyautogui.leftClick(x=2100, y=714)
            print('leftClick')
            pyautogui.dragTo(164,714, 0.2)
            print('dragLeft')
            print('\n')
            # Loop 2
            pyautogui.leftClick(x=2100, y=314)
            print('leftClick')
            pyautogui.dragTo(164,314, 0.2)
            print('dragLeft')
            print('\n')
            pyautogui.leftClick(x=164, y=714)
            print('leftClick')
            pyautogui.dragTo(2100,714, 0.2)
            print('dragRight')
            print('\n')
            # Click
            pyautogui.leftClick(1395, 1023)
            print('click')
            print('\n')
            if keyboard.is_pressed('F7'):    
                break