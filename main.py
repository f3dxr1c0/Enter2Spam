import time
import random
import pyautogui as pg
from colorama import Fore
import os

os.system('title WhatsApp Spammer')

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def whatsapp_spammer():
  message = input("MSG: ")
  t = int(input("How many times?: "))
  time.sleep(0.10)
  print(Fore.RED + 'Preparing in 10 seconds...' + Fore.RESET)
  for i in range(t):
    msg = random.choice(message)
    pg.write(msg)
    pg.press('enter')

while True:
  print(Fore.GREEN + '''
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
      ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                                                                                                                                                                                                                          
          [1] START (Press 'ENTER')                   ''' + Fore.RESET)

  choice = input()

  if choice == '1':
   whatsapp_spammer()
   clear()
 
  else:
   print(Fore.RED + 'INVALID INPUT' + Fore.RESET)
   clear()
