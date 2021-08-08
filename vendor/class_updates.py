import requests
import time
from tqdm import tqdm
from colorama import Fore
import sys, os


banner = Fore.LIGHTYELLOW_EX+"""
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""


def __start__():
    try:
        world = requests.get("https://code-irans.github.io/updates_passwd/README.md").text

        print(Fore.LIGHTYELLOW_EX+"Downloading Updates Anywehre... \n")

        for i in tqdm(range(5)):
            time.sleep(2)
        
        os.system("cls" or "clear")

        print(banner)

        print(Fore.WHITE+"-"*40)

        print("\n" + world)
    except KeyboardInterrupt:
        print(Fore.RED+"Ctrl + C [exited]")
        sys.exit()

