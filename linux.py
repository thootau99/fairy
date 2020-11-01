import pyautogui as pa
import time
while True:
  pa.keyDown('f6')
  pa.keyUp('f6')

  time.sleep(0.1)

  pa.mouseDown()
  pa.mouseUp()