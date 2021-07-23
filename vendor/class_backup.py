from colorama import Fore
import time

def __backup__():
    a = open("logs/work/passwd.key" , "r").read()

    if a == "":
        wcs = input(Fore.LIGHTYELLOW_EX+"This is Enter Password Main : ")

        files = open("logs/work/passwd.key" , "a")

        files.write(wcs)

        print(Fore.GREEN+"Please Save Password...")

        time.sleep(3)

        print(Fore.LIGHTGREEN_EX+"Succsessful Save Passowrd!")


    else:

        wd = input(Fore.GREEN+"Enter Login Password : ")

        p = open("logs/work/passwd.key" , "r").read()

        if wd == p:

            rot = input(Fore.RED+"Bakup you want the passwords cleared (n, y) ? ")

            if rot == "y":
                f = open("logs/rep.txt" , "r").read()
                r = open("password.txt" , "a")

                r.write(f)

                print(Fore.GREEN+"Please Backup Password...")

                time.sleep(3)

                print(Fore.LIGHTGREEN_EX+"Succsessful Backup Passowrd!")
        else:
            print(Fore.RED+"Not Login System Backup!")


