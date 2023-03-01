from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

# create a list of filepaths
filepaths = glob.glob("files/*.txt")
# create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# go through each text file
for filepath in filepaths:
    # add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and conver it to a title case(e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    # add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

    # Get the content of each text file
    with open(filepath, 'r') as file:
        content = file.read()
    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# produce the PDF
pdf.output("output.pdf")
