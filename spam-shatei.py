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

print("            SHATEI SPAM")
print("            code: Shatei")      
print("            creditos: Shatei")         
print("  COLE O TOKEN E O ID CERTO SE N NAO IRA FUNCIONAR")
print("  A FERRAMENTA N RECONHECE SE ESTA CERTO O TOKEN")
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
