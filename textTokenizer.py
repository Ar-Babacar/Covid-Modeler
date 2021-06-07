import PyPDF2 as pdf
import sys, re, operator, itertools, shutil, time
#import numpy as np
#import pandas as pd
import os, os.path
from os import listdir
#import win32api


#file = open(path + file, 'rb')
#covid = pdf.PdfFileReader(file)
#covidpg1 = covid.getPage(0)
#covidpg1 = covidpg1.extractText()
#Nbr_Communique = re.search('Communique(\d+)', covidpg1)
#Date = re.search((r'(\s+ \d+ \s+ \d+)', covidpg1))

path='/Users/babacar/Covid-Modeler/dataAcquisition/Text'
helper = range(1, 92)
a = dict()
for files, i in zip(path, helper):
    with open('/Users/babacar/Covid-Modeler/dataAcquisition/Text/Com417.txt') as f:
        covid =f.read()

Nbr= re.findall('COMMUNIQUE +(\d+)', covid)
Label_Communique = re.findall('COMMUNIQUE', covid)
reg= re.findall('Dakar +(\d+)', covid)
date =re.findall('Ce + \s+ \d+', covid)
match = re.search(r'\s{4}-\d{2}-\d{2}', covid)
Date = re.search((r'(\s+ \d+ \s+ \d+)'), covid)

print(Label_Communique )
print(Nbr )
print(reg)
print(date)
