from colorama import Fore
import time, os


banner = Fore.LIGHTYELLOW_EX+"""
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

def __reseting__():
    any = input(Fore.LIGHTYELLOW_EX+"Restet Password Maker you want the passwords cleared (n, y) ? ")

    if any == "y":
        passwd = open("logs/work/passwd.key" , "r+")
        rep = open("logs/rep.txt" , "r+")
        password = open("password.txt" , "r+")

        passwd.truncate(0)
        rep.truncate(0)
        password.truncate(0)

        print(Fore.GREEN+"Please Reset Home File...")

        time.sleep(4)

        os.system("cls" or "clear") 

        print(banner)       

        print(Fore.RESET+"Sucsessful Reseting Password Maker!")
