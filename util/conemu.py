# on 02 Jun 2020 
import pyautogui
import time
pyautogui.FAILSAFE = False

def open_conemu():
    pyautogui.click(30, 350)
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'e')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'shift', 'o')
    time.sleep(3)

def block_1():
	pyautogui.hotkey('ctrl', '1')
	time.sleep(0.2)

def block_2():
	pyautogui.hotkey('ctrl', '2')
	time.sleep(0.2)

def block_3():
	pyautogui.hotkey('ctrl', '3')
	time.sleep(0.2)

def flask_run(port=4010):
    pyautogui.typewrite('flask run --host=0.0.0.0 --port=' + str(port) + '\n')

def yarn_dev():
	pyautogui.typewrite('yarn dev\n')

def open_vscode():
	pyautogui.typewrite('code .\n')

def go_aplication_path():
	pyautogui.typewrite('cd D:/Documents/\n')
	pyautogui.typewrite('cd aplication/\n')

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