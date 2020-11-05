#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 14 Jul 2020 
import pyautogui
import time
import util.dbeaver as db
import util.docker as docker
import util.terminator as terminator
pyautogui.FAILSAFE = False

if (__name__ == "__main__"):
  terminator.block_4()
  terminator.go_authentication_app()

  terminator.block_3()
  terminator.close_yarn_dev()
  terminator.go_authentication_app()
  terminator.yarn_dev()

  terminator.block_2()
  docker.down_docker()
  terminator.go_authentication_api()
  docker.up_docker()
  
  terminator.block_4()
  terminator.open_vscode()
