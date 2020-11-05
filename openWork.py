#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 02 Jun 2020 
import pyautogui
import time
import platform
import util.terminator as terminator
import util.conemu as conemu
import util.docker as docker
import updateBack
pyautogui.FAILSAFE = False

def linux():
  password = pyautogui.password(text='A senha da VPN, my Lord.', title='Senha', default='', mask='*')
  if password:
    option = pyautogui.confirm(text='My Lord, deseja atualizar o back?', title='Atualizção', buttons=['Sim', 'Não'])
    time.sleep(1)
    terminator.open_terminator()
    terminator.block_3()
    terminator.go_workflowpag_front()
    terminator.yarn_dev()
    terminator.block_2()
    terminator.go_workflowpag_api()
    docker.up_docker(False)
    terminator.block_4()
    terminator.go_workflowpag_front()
    terminator.open_vscode()
    terminator.block_1()
    terminator.open_vpn_path()
    terminator.block_1()
    terminator.vpn_command()
    terminator.put_email()
    terminator.put_password(password)
    if option=='Sim':
      time.sleep(2)
      updateBack.run(sleepPlus=10, is_openWork=True)

def windows():
  conemu.open_conemu()
  conemu.go_workflowpag_api()
  conemu.flask_run()
  conemu.block_2()
  conemu.go_workflowpag_front()
  conemu.yarn_dev()
  conemu.block_1()
  conemu.go_workflowpag_front()
  conemu.open_vscode()


if (__name__ == "__main__"):
  so = platform.system()
  if so == 'Windows':
    windows()
  elif so == 'Linux':
    linux()
  else:
    print('Sistema não identificado.')
    