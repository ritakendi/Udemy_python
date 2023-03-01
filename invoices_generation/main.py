import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# create a list since we have multiple files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # create a pdf document
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # add a page to the document
    pdf.add_page()

    filename = Path(filepath).stem
    # get invoice number from the filename
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    # write invoice_nr inside the pdf document.
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")

    pdf.output(f"PDF's/{filename}.pdf")
