from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import pandas as pd
import os
import time


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


# if __name__ == '__main__':
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

    for j, rows in data.iterrows():
        i += 1
        pdf2 = PdfFileWriter()
        set_need_appearances_writer(pdf2)
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        # Key = pdf_field_name : Value = csv_field_value
        field_dictionary_1 = {  # file_content
            "InvestorNazev": rows['Investor'],
            "MistoStavby": rows['MistoStavby'],
            "Akce": rows['Akce'],
            "Vykres": rows['Vykres'],
        }

        # print(field_dictionary_1)
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

 if __name__ == "__main__":
   filler()