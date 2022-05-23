
import os

import time
from welcome import mainmenu

#pokud poběží na windows tak os.system("cls") jinak ("clear")

def main():
    while(True):
        os.system("cls")
        print(mainmenu("SrotoApp"))
        print("\nVyber si co chceš udělat : ")
        print("""
        1 : Kovertovat z xls do csv
        2 : Vyplnit pdf formulář
        konec : Konec aplikace
        """)
        choice = input("\nVyber volbu : ")

        if choice == '1':
            os.system("python .\konvert.py")
            os.system("cls")
        elif choice == '2':
            os.system("python .\/filler.py")
        elif choice == 'konec':
            #print("vybral jsi 3")
            exit()
        else:
            print("Zadaná volba neexistuje")
            time.sleep(1.0)
        os.system("cls")

if __name__ == "__main__":
    main()