#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 02 Jun 2020 
import pyautogui
import time
pyautogui.FAILSAFE = False


def rm_migrations():
  # Comando 'rm -rf migrations/'
  pyautogui.typewrite('rm -rf mi')
  pyautogui.press(['tab', 'enter'])

def flask_init():
  # Comando 'flask db init'
  pyautogui.typewrite('flas')
  pyautogui.press('tab')
  pyautogui.typewrite('db init\n')

def flask_initial():
  # Comando 'flask db migrate -m "Initial"'
  pyautogui.typewrite('flas')
  pyautogui.press('tab')
  pyautogui.typewrite('db migrate -m "Initial"\n')

def flask_upgrade_heads():
  # Comando 'flask db upgrade heads'
  pyautogui.typewrite('flas')
  pyautogui.press('tab')
  pyautogui.typewrite('db upgrade heads\n')

def flask_seed():
  # Comando 'flask seed'
  pyautogui.typewrite('flas')
  pyautogui.press('tab')
  pyautogui.typewrite('seed\n')

def exit_commands():
  # Comando 'exit'
  pyautogui.typewrite('exit\n')

def flask_commands():
  rm_migrations()
  flask_init()
  flask_initial()
  flask_upgrade_heads()
  flask_seed()
  exit_commands()

def open_dash():
	# Entrar no BASH
  pyautogui.typewrite('doc')
  pyautogui.press('tab')
  pyautogui.typewrite(' exe')
  pyautogui.press('tab')
  pyautogui.typewrite('-it w')
  pyautogui.press('tab')
  pyautogui.typewrite(['a','tab'])
  pyautogui.typewrite(' bash\n')
  time.sleep(1)

def up_docker(sleep=True):
	# Subir docker-compose
  pyautogui.typewrite('doc')
  pyautogui.press('tab')
  pyautogui.typewrite(['-','c','tab'])
  pyautogui.typewrite('up --b')
  pyautogui.press(['tab','-','d','enter'])
  if sleep:
    time.sleep(5)

def down_docker():
	# Descer docker e git pull
  pyautogui.typewrite('doc')
  pyautogui.press('tab')
  pyautogui.typewrite(['-','c','tab'])
  pyautogui.typewrite(['d','tab','enter'])
  time.sleep(15)
