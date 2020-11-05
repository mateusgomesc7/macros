#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 02 Jun 2020 
import pyautogui
import time
import util.dbeaver as db
import util.docker as docker
import util.terminator as terminator
pyautogui.FAILSAFE = False	

def run(sleepPlus = 0, is_openWork=False):
	is_db_open = False
	
	if not is_openWork:
		is_db_open = pyautogui.confirm(text='O DBeaver já está aberto, My Lord?', title='Abrir DBeaver', buttons=['Sim', 'Não'])
		time.sleep(2)

	if not is_db_open or is_db_open=='Não':
		db.open_dbeaver()

	terminator.block_2()
	docker.down_docker()
	
	time.sleep(sleepPlus)
	db.open_screen()
	db.close_windows(5)

	terminator.block_2()
	terminator.git_pull()
	docker.up_docker()
	
	db.master.connect()
	db.workflow.disconnect()	

	db.workflow.drop()
	db.workflow.create()
	db.workflow.connect()

	terminator.block_2()
	docker.open_dash()
	docker.flask_commands()

if (__name__ == "__main__"):
	run()
