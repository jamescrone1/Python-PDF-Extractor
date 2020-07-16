import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBoxHorizontal

from io import StringIO


# PDFMiner method
def pdfminer_pdf_text(file_path):
    with open(file_path, 'rb') as f:
        lines = []
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(f):
            interpreter.process_page(page)
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal):
                    lines.extend(element.get_text().splitlines())
        text = ""
        for line in lines:
            text += line
        return text


# PyPDF2 method
def pdf2_pdf_text(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        num_pages = pdf_reader.numPages
        count = 0
        text = ""

        while count < num_pages:
            page_obj = pdf_reader.getPage(count)
            count += 1
            text += page_obj.extractText()

        if text != "":
            text = text

    return text
