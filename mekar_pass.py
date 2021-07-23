import string
from random import *
import os
from colorama import Fore
import sys
import time

from vendor import class_backup
from vendor import class_updates

char = string.ascii_letters + string.punctuation + string.digits

os.system("cls" or "clear")

print("")

banner = Fore.LIGHTYELLOW_EX+"""
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

Lanf = 8
Mode = 10



def passwd(txt , max):
    password_1 = "".join(choice(char) for x in range(randint(Lanf, Mode)))
    password_2 = "".join(choice(char) for x in range(randint(Lanf, Mode)))
    password_3 = "".join(choice(char) for x in range(randint(Lanf, Mode)))
    password_4 = "".join(choice(char) for x in range(randint(Lanf, Mode)))


    os.system("cls" or "clear")

    time.sleep(0.1)
    print(Fore.YELLOW+"[1] " +Fore.GREEN+"This Your Password : ", txt + password_1 + max)
    time.sleep(0.1)
    print(Fore.YELLOW+"[2] " +Fore.GREEN+"This Your Password : ", txt + password_2 + max)
    time.sleep(0.1)
    print(Fore.YELLOW+"[3] "+Fore.GREEN+"This Your Password : ", txt + password_3 + max)
    time.sleep(0.1)
    print(Fore.YELLOW+"[4] "+Fore.GREEN+"This Your Password : ", txt + password_4 + max)
    time.sleep(0.1)
    print(Fore.WHITE)

    form = input(Fore.LIGHTRED_EX+"Enter Options List : ")

    if form == "1":
        os.system("cls" or "clear")
        print(Fore.CYAN+"Password Maker : " + txt + password_1 + max)
        print(Fore.MAGENTA+"Saved Password To 'password.txt'")
        a = open("password.txt" , "a")
        a.write(txt + password_1 + max + "\n")

    elif form == "2":
        os.system("cls" or "clear")
        print(Fore.CYAN+"Password Maker : " + txt + password_2 + max)
        print(Fore.MAGENTA+"Saved Password To 'password.txt'")
        a = open("password.txt" , "a")
        a.write(txt + password_2 + max + "\n")

    elif form == "3":
        os.system("cls" or "clear")
        print(Fore.CYAN+"Password Maker : " + txt + password_3 + max)
        print(Fore.MAGENTA+"Saved Password To 'password.txt'")
        a = open("password.txt" , "a")
        a.write(txt + password_3 + max + "\n")

    elif form == "4":
        os.system("cls" or "clear")
        print(Fore.CYAN+"Password Maker : " + txt + password_4 + max)
        print(Fore.MAGENTA+"Saved Password To 'password.txt'")
        a = open("password.txt" , "a")
        a.write(txt + password_4 + max + "\n")
    


def create_passwd():
    tick = input("Enter Text To Password : ")
    max = input("Enter Max To Password : ")

    input("This Anyting...")

    passwd(tick, max)

def viwe_passwd():

    file = open("password.txt" , "r").read()
    print(Fore.LIGHTYELLOW_EX+"View Password Filer. \n")
    print(Fore.WHITE+"-"*30)
    print(file)

def reset_file():
    ret = input(Fore.RED+"Sure you want the passwords cleared (n, y) ? ")

    if ret == "y":
        dir = open("password.txt" , "r").read()

        syn = open("logs/rep.txt" , "a")

        syn.write(dir)

        restet_dir = open("password.txt" , "r+")
        restet_dir.truncate(0)

        print(Fore.RED+"\n[!] Reseting Password !!!")



try:

    print(banner)

    time.sleep(0.1)
    print(Fore.RED+"[1] "+Fore.GREEN+"Acsess Make Password! \n")
    time.sleep(0.1)
    print(Fore.RED+"[2] "+Fore.GREEN+"Acsess View Saved Passowrd! \n")
    time.sleep(0.1)
    print(Fore.RED+"[3] "+Fore.GREEN+"Acsess Reset List Password! \n")
    time.sleep(1.0)
    print(Fore.RED+"[4] "+Fore.GREEN+"Acsess Backup List Password! \n")
    time.sleep(1.0)
    print(Fore.RED+"[5] "+Fore.GREEN+"Acsess Update Maker Lists! \n")
    

    opt = input(Fore.LIGHTYELLOW_EX+"\n\nEnter Options \n  >>> ")

    if opt == "1":
        os.system("cls" or "clear")
        print(banner)
        create_passwd()

    elif opt == "2":
        os.system("cls" or "clear")
        print(banner)
        viwe_passwd()

    elif opt == "3":
        os.system("cls" or "clear")
        print(banner)
        reset_file()
    elif opt == "4":
        os.system("cls" or "clear")
        print(banner)
        class_backup.__backup__()
    elif opt == "5":
        os.system("cls" or "clear")
        print(banner)
        class_updates.__start__()

except KeyboardInterrupt:
    print(Fore.RED+"\nCtrl + C [Exited]")
    sys.exit()