#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 02 Jun 2020 
import pyautogui
import time
pyautogui.FAILSAFE = False

class database:
	def __init__(self, x, y, name, master=None):
		self.x = x
		self.y = y
		self.name = name
		self.master = master

	def click(self, xAux = 0, yAux = 0):
		pyautogui.click(self.x + xAux, self.y + yAux)
	def right_click(self, xAux = 0, yAux = 0):
		pyautogui.rightClick(self.x + xAux, self.y + yAux)

	def connect(self):
		self.click()
		self.right_click()
		time.sleep(0.25)
		self.click(70, 170)
		time.sleep(1)
		# Um clique fora
		self.click(-50, 150)

	def disconnect(self):
		self.click()
		self.right_click()
		time.sleep(0.25)
		self.click(70, 220)
		time.sleep(1)
		# Um clique fora
		self.click(-50, 150)

	def btn_new_script(self):
		pyautogui.click(500, 420)
		time.sleep(2)
		self.click(550, -60)

	def btn_dont_save(self):
		pyautogui.click(650, 580)

	def new_scripts(self):
		if self.master:
			self.master.click()
			self.master.right_click()
			time.sleep(0.20)
			self.master.click(70, 20)
			time.sleep(0.50)
			self.btn_new_script()
		else:
			print('Este database não tem master')
			exit()

	def run_script(self):
		time.sleep(1.2)
		pyautogui.hotkey('ctrl', 'enter')
		time.sleep(3)
		pyautogui.hotkey('ctrl', 'w')
		time.sleep(0.25)
		self.btn_dont_save()
		time.sleep(0.25)
	
	def drop(self):
		self.new_scripts()
		pyautogui.typewrite('DROP DATABASE ' + self.name + '\nGO')
		self.run_script()

	def create(self):
		self.new_scripts()
		pyautogui.typewrite('CREATE DATABASE ' + self.name + '\nGO')
		self.run_script()


master = database(150, 260, 'master')
workflow = database(150, 280, 'Workflow', master)

def close_windows(number=1):
    pyautogui.keyDown('ctrlleft')
    for i in range(number):
	    pyautogui.keyDown('w')
	    pyautogui.keyUp('w')
	    time.sleep(0.25)
    pyautogui.keyUp('ctrlleft')
    time.sleep(0.25)

def open_dbeaver():
	# Abrir DBeaver
	pyautogui.click(36, 339)
	time.sleep(1)

def open_screen():
	# Abrir janela do DBeaver
	pyautogui.press('winleft')
	time.sleep(2.2)
	pyautogui.typewrite('dbe\n')
	time.sleep(0.5)
	pyautogui.hotkey('winleft', 'left')
	time.sleep(5)

def new_scripts():
	# Abrir seleção de script
	pyautogui.click(231, 262)
	pyautogui.rightClick(231, 262)
	time.sleep(0.20)
	pyautogui.click(249, 279)
	time.sleep(0.5)
	pyautogui.click(520, 415)

def btn_dont_save():
	pyautogui.click(650, 580)

def drop_workflow():
	new_scripts()
	# drop workflow
	time.sleep(1)
	pyautogui.typewrite('drop database Workflow\nGO')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'enter')
	time.sleep(3)
	close_windows()
	btn_dont_save()
	
def create_workflow():
	new_scripts()
	# create workflow
	time.sleep(1)
	pyautogui.typewrite('CREATE DATABASE Workflow\nGO')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'enter')
	time.sleep(3)
	close_windows()
	btn_dont_save()

def run_scripts():
    drop_workflow()
    create_workflow()
