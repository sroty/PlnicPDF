from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import pandas as pd

def convertFile():
    file_path = fd.askopenfilename(title="select", filetypes=[("Excel files", "*.xlsx"), ("Excel files 97-2003", "*.xls")])
    global path
    path = file_path

    read_file = pd.read_excel(path)
    read_file.to_csv(r"test.csv", index=None, header=True)