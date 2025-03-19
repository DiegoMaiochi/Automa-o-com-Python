import pyautogui as pa
import time
pa.PAUSE = 1

pa.press('win')
pa.write("google chrome")
pa.press('ENTER')
pa.write("github.com")
pa.press('ENTER')
time.sleep(2)

pa.press('Tab', presses= 11)
pa.press('ENTER')
pa.write("diegomaiochi")
pa.press('ENTER')
time.sleep(3)

pa.press('Tab', presses= 3)
pa.press('ENTER')