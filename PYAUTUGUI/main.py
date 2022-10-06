import pyautogui
import time


time.sleep(5)
# n=0
m=0
while m<700:

    # f = open('para.txt', 'r')
    # text = f.read().split('\n')

    # for lines in text:
    # pyautogui.write('🥚', interval=0)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    m+=1
        # n+=1
