import requests
from pathlib import Path
import sys
import ssl
from socket import timeout
from urllib.parse import quote
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.parse import unquote
from urllib.request import urlopen
import urllib.request 
import os
import ocrmypdf

URL ='https://sante.sec.gouv.sn/Présentation/coronavirus-informations-officielles-et-quotidiennes-du-msas'

def get_pdfs(my_url):
    links = []
    timeout= 15*1000000
    context = ssl._create_unverified_context()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    req= urllib.request.Request(my_url,data=None, headers=headers)
    html = urlopen(req,context=context,timeout=timeout).read()
    html_page = bs(html, features="lxml") 
    og_url = html_page.find("meta",  property = "og:url")
    base = urlparse(unquote(my_url))
    print("base",base)

    for link in html_page.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('pdf'):
            if "sitrep" not in current_link:
                if og_url:
                    print("currentLink",current_link)
                    links.append(og_url["content"] + current_link)
                else:
                    print(current_link)
                    links.append(current_link)           
    for link in links:
        num = ''.join(filter(lambda i: i.isdigit(), link))
        filename = Path('./dataAcquisition/Pdf/com'+str(num[:-2])+'.pdf')

        try: 
            response=requests.get(link,headers=headers)

            filename.write_bytes(response.content)
            os.system(f'ocrmypdf {filename} {filename}')
        except Exception as e:
            print("Could not download file {}".format(link))
            print(e)
            sys.exit()

    print('\n')

def main():
    get_pdfs(quote_plus(URL,safe='/:#?=&'))

main()
