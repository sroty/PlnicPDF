from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import pandas as pd
import os
from welcome import konvert
import time


root = Tk()
root.withdraw()

while(True):

        os.system("cls")
        print(konvert("ConvertoApp"))
        print("\nVyber si co chceš udělat : ")
        print("""
        1 : Vybrat soubor pro převod do csv
        2 : Spustit převod
        3 : Konec apky
        """)
        choice = input("\nVyber volbu : ")

        if choice == '1':

            file_path = fd.askopenfilename(title="select", filetypes=[("Excel files", "*.xlsx"), ("Excel files 97-2003", "*.xls")])
            root.update()

            path = file_path
            print("Vybral jsi : \n" + path)
            input("Pokračuj stisknutím enteru... ")



        elif choice == '2':
            print("Zadej budoucí název csv souboru: ")
            csv_name = input()
            while csv_name == "":
                print("Zadej název souboru, jinak se nepohneš: ")
                csv_name = input()
            else:
                read_file = pd.read_excel(path)
                read_file.to_csv(fr"In/{csv_name}.csv", index=NONE, header=True)
                print("Soubor byl převeden")
                time.sleep(2.0)
        elif choice == '3':
            exit()


        os.system("cls")









