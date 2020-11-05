#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 02 Jun 2020 
import pyautogui
import time
pyautogui.FAILSAFE = False

def open_terminator():
	# Abrir terminator
	pyautogui.click(46, 474)
	time.sleep(2)
	pyautogui.hotkey('winleft', 'right')
	time.sleep(2)
	pyautogui.hotkey('ctrl', 'shift', 'o')
	pyautogui.hotkey('ctrl', 'shift', 'e')
	pyautogui.hotkey('ctrl', 'shift', 'n')
	pyautogui.hotkey('ctrl', 'shift', 'e')

def block_1():
	pyautogui.click(1659, 101)
	time.sleep(0.2)

def block_2():
	pyautogui.click(2438, 413)
	time.sleep(0.2)

def block_3():
	pyautogui.click(1707, 627)
	time.sleep(0.2)

def block_4():
	pyautogui.click(2079, 642)
	time.sleep(0.2)

def git_pull():
	#git pull
	pyautogui.typewrite('git pull\n')
	time.sleep(5)

def yarn_dev():
	pyautogui.typewrite(['y','a','tab'])
	pyautogui.typewrite(' dev\n')

def close_yarn_dev():
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(2)

def open_vscode():
	pyautogui.typewrite('code .\n')
	time.sleep(3)
	pyautogui.hotkey('winleft', 'left')
	time.sleep(2)

def open_vpn_path():
	# Entrar na pasta da vpn
	pyautogui.typewrite('cd Doc')
	pyautogui.press('tab')
	pyautogui.typewrite(['a','p','tab', 'enter'])

def vpn_command():
	# Comando levantar VPN
	pyautogui.typewrite('sudo openvpn Asse')
	pyautogui.typewrite(['tab', 'enter'])
	time.sleep(2)
	pyautogui.typewrite('1504\n')
	time.sleep(1)

def put_email():
	pyautogui.typewrite('mateus.correia@assert.ifpb.edu.br\n')

def put_password(password):
	pyautogui.typewrite(password)
	time.sleep(1)
	pyautogui.press('enter')

def go_aplication_path():
	pyautogui.typewrite('cd /home/mateus/Documentos/aplications/\n')

def go_workflowpag_front():
	go_aplication_path()
	pyautogui.typewrite(['c','d',' ','w','tab','f','tab','enter'])

def go_workflowpag_api():
	go_aplication_path()
	pyautogui.typewrite(['c','d',' ','w','tab','a','tab','enter'])

def go_authentication_app():
	go_aplication_path()
	pyautogui.typewrite('cd au')
	pyautogui.press('tab')
	pyautogui.typewrite(['w','tab','p','tab','enter'])

def go_authentication_api():
	go_aplication_path()
	pyautogui.typewrite('cd au')
	pyautogui.press('tab')
	pyautogui.typewrite(['w','tab','i','tab','enter'])
