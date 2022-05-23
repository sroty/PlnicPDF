from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from tkinter import *
from tkinter import filedialog as fd
import pandas as pd
import os
from welcome import plnic
import time

root = Tk()
root.withdraw()

def set_need_appearances_writer(writer: PdfFileWriter):
    try:
        catalog = writer._root_object
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})
        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

def filler():
    print(file_path_pdf, file_path)
    csv_filename = file_path
    pdf_filename = file_path_pdf

    csvin = os.path.normpath(os.path.join(os.getcwd(), '', csv_filename))
    pdfin = os.path.normpath(os.path.join(os.getcwd(), '', pdf_filename))
    pdfout = os.path.normpath(os.path.join(os.getcwd(), 'Out'))
    data = pd.read_csv(csvin)
    pdf = PdfFileReader(open(pdfin, "rb"), strict=False)
    if "/AcroForm" in pdf.trailer["/Root"]:
        pdf.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_fields = [str(x) for x in pdf.getFields().keys()]  # List of all pdf field names
    csv_fields = data.columns.tolist()

    i = 0  # Filename numerical prefix


    field_dictionary_1 = {
    }
    for j, rows in data.iterrows():
        i += 1
        pdf2 = PdfFileWriter()
        set_need_appearances_writer(pdf2)
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        for col in data.columns:
            #print(col)
            #print(rows[col])
            field_dictionary_1[col] = rows[col]



        #print(type(field_dictionary_1))

        temp_out_dir = os.path.normpath(os.path.join(pdfout, str(i) + 'out.pdf'))
        pdf2.addPage(pdf.getPage(0))
        pdf2.updatePageFormFieldValues(pdf2.getPage(0), field_dictionary_1)
        # pdf2.addPage(pdf.getPage(1))
        # pdf2.addPage(pdf.getPage(2))
        # pdf2.addPage(pdf.getPage(3))
        outputStream = open(temp_out_dir, "wb")
        pdf2.write(outputStream)
        outputStream.close()
    print(f'Operace dokončena: {i} PDF zpracováno!')
    time.sleep(3.0)
    # print(field_dictionary_1)

# if __name__ == "__main__":
 #  filler()


while(True):

    os.system("cls")
    print(plnic("FillerApp"))
    print("\nCo budeš dělat : ")
    print("""
    1 : Vyber soubor ve formátu csv
    2 : Vyber šablonu ve formátu pdf
    3 : Spustit plnič
    4 : Hotovo
    """)
    choise = input("\nVyber volbu : ")

    if choise == '1':
        file_path = fd.askopenfilename(title="select", filetypes=[("Čárkou oddělené hodnoty", "*.csv")])
        root.update()

        print("Vybral jsi : \n" + file_path)
        input("Pokračuj stisknutím enteru...")


    elif choise == '2':
        file_path_pdf = fd.askopenfilename(title="select", filetypes=[("Soubor ve formátu pdf", "*.pdf")])
        root.update()
        #pdf_file = Path(file_path_pdf).name

        print("Vybral jsi : \n" + file_path_pdf)
        input("Pokračuj stisknutím enteru...")

    elif choise == '3':
        filler()


    elif choise == '4':
        exit()

    os.system("cls")
