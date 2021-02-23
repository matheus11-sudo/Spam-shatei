import requests
import os
import time
import platform
from colorama import Fore
import sys
import random

platform = platform.system()
menu = sys.argv[1::]
if platform == 'Windows':
	os.system('cls')
else:
	os.system('clear')

print(" ____________________________________")
print(" | ")
print(" |      \033[33m      ___________ \033[m         ")
print(" |           \033[33m/SHATEI SPAM\ \033[m")
print(" |       \033[33m    \___________/ \033[m")
print(" |       \033[33m     %%%%%%%%%%%	\033[m  ")
print(" |")
print(" |            ____________")
print(" |            \033[41mCODE: Shatei\033[m ")
print(" |")
print(" |           _______________")
print(" |           \033[36mCREDITOS: Shatei\033[m \n")       
        
print("  COLE O TOKEN E O ID CERTO SE N NAO IRA FUNCIONAR")
print("  A FERRAMENTA N RECONHECE SE ESTA CERTO O TOKEN")
token = str(input("\n  COPIE SEU TOKEN E COLE NO TERMINAL \n"))
id = (input("\n  COLE O ID DO CANAL \n"))
mensagem = input("\nQUAL SERA A MENSAGEM? \n")

def spam():
	payload
