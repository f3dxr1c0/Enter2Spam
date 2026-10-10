from pystyle import Colors, Colorate, Center
from colorama import Fore
import pyautogui as pg
import keyboard
import time
import os

os.system("title Enter2Spam")

def clear():
    os.system("cls")

def main():
    clear()
    print(Colorate.Horizontal(Colors.green_to_white, '''

                                                                        
 ▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄                      
███▀▀▀▀▀        ██               ▀▀▀▀████ █████▀▀▀                      
███▄▄    ████▄ ▀██▀▀ ▄█▀█▄ ████▄    ▄██▀   ▀████▄  ████▄  ▀▀█▄ ███▄███▄ 
███      ██ ██  ██   ██▄█▀ ██ ▀▀  ▄███▄▄▄    ▀████ ██ ██ ▄█▀██ ██ ██ ██ 
▀███████ ██ ██  ██   ▀█▄▄▄ ██    ████████ ███████▀ ████▀ ▀█▄██ ██ ██ ██ 
                                                   ██                   
                                                   ▀▀   
    [1] Messages to spam
    [2] Help
    [3] Exit                

'''))

    e2s = input(Colorate.Horizontal(Colors.green_to_white, "\nOpt > "))

    if e2s == '1':
        clear()
        print(Fore.GREEN + Center.XCenter("=" * 50))
        print(Center.XCenter("Enter2Spam - Spam"))
        print(Fore.GREEN + Center.XCenter("=" * 50))
        msg = input(Fore.YELLOW + "Messages to spam: ")
        t = int(input(Fore.YELLOW + "How many times: "))
        print("You have 5 seconds to click on the chat where you want to spam...")
        time.sleep(5)
        for i in range(t):
            if keyboard.is_pressed('esc'):
                print("Stopped.")
                break
            pg.write(msg)
            time.sleep(0.1)
            pg.press('enter')
        main()

    elif e2s == '2':
        clear()
        print(Fore.GREEN + Center.XCenter("=" * 50))
        print(Center.XCenter("Enter2Spam - Help"))
        print(Center.XCenter("=" * 50) + Fore.RESET)
        print(Fore.YELLOW + '''

    [1] Messages to spam ---> Insert the messages to spam and how many times you want to send
    [2] Help             ---> Show this message
    [3] Exit             ---> Exit to the program

    When you insert the 1's opts, and have already insert the messages and the time you want to send it, you have to go\n    in the chat where you want to send, click 'ENTER' and waiting 5 seconds.
    
    If the program is still sending the messages (cause bug or the times is too large) click 'ESC' and it will stop.
''' + Fore.RESET)
        print(Center.XCenter(Fore.GREEN + "=" * 100))
        input(Center.XCenter("\nClick 'ENTER' to back to menu..."))
        clear()
        main()

    elif e2s == '3':
        clear()
        print(Fore.GREEN + Center.XCenter("=" * 50))
        print(Center.XCenter("Enter2Spam - Exit"))
        print(Fore.GREEN + Center.XCenter("=" * 50))
        print(Fore.YELLOW + Center.XCenter("\nThanks for using Enter2Spam!\n"))
        input(Center.XCenter("\nClick 'ENTER' to exit..."))
        clear()
        exit()

if __name__ == "__main__":
    main()
