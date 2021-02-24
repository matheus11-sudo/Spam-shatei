import requests
import os
import time
import platform
from colorama import Fore
import sys
import random

latform = platform.system()
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
print("  \033[37mCOLE O TOKEN E O ID CERTO SE N NAO IRA FUNCIONAR\033[m")
print("  \033[37m A FERRAMENTA N RECONHECE SE ESTA CERTO O TOKEN\033[m")
token = str(input("\n  COPIE SEU TOKEN E COLE NO TERMINAL \n"))
id = (input("\n  COLE O ID DO CANAL \n"))
mensagem = input("\nQUAL SERA A MENSAGEM? \n")

def spam():
	payload = {
		'content': mensagem
	}
	
	header = {'authorization': token
	}
	
	r =	requests.post("https://discord.com/api/v8/channels/" + id + "/messages", data=payload, headers=header)
	
	print("mensagem enviada")

while True:
	print(spam())
	print(spam())
