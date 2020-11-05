#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 14 Jul 2020 
import pyautogui
pyautogui.FAILSAFE = False

if (__name__ == "__main__"):
  print('Press Ctrl-C to quit.')
  try:
      while True:
          x, y = pyautogui.position()
          positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
          print(positionStr, end='')
          print('\b' * len(positionStr), end='', flush=True)
  except KeyboardInterrupt:
      print('\n')