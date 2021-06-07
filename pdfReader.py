import os
import pdfplumber
import ocrmypdf
import tabula
import PyPDF2
import textract
import re

covid='/Users/babacar/Covid-Modeler/dataAcquisition/Pdf/com417.pd
doc = textract.process(r"/Users/babacar/Covid-Modeler/dataAcquisition/Pdf/com417.pdf", encoding = 'utf-8')
f = open('pdf_to_text.txt','wb')
f.write(doc)

