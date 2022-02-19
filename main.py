import pyautogui as pg
import time

time.sleep(10)

for i in range(150):
    pg.write('Hello World!')
    pg.press('Enter')
