import csv
from IPython import display
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time



##table of contents scraper===========================================================


urlTableOfContents = 'https://plato.stanford.edu/contents.html'
reqContents = requests.get(urlTableOfContents)
contentTableOfContents = BeautifulSoup(reqContents.text, 'html.parser')
div_content = contentTableOfContents.find('div', id='content')


entriesToC = []
entriesLinks = []
entriesAutomate = []


for href in div_content.find_all('a', href=True):
    entriesToC.append([href.text, href.get('href')])
    entriesAutomate.append(href.get('href'))
    # print(href.text)

#csv writer
df = pd.DataFrame(entriesToC, columns=['Entry Title', 'Link'])
df.to_csv('tableOfContents.csv', encoding='utf-8-sig')

df2 = pd.DataFrame(entriesAutomate, columns=['HREF'])
df2.to_csv('letstrythis.csv', encoding='utf-8-sig')

# ##individual page bib scarper-------------------------------------------------------------------
# with open('allBibNewTest.csv', 'w') as outfile:
#     writer = csv.writer(outfile)

for x in entriesAutomate:

    urlIndividual = f'https://plato.stanford.edu/{x}/'
    if x == 'projected-contents.html':
        break

    if x == '#pagetopright':
        continue



    else:
        reqIndividual = requests.get(urlIndividual)
        contentIndividual = BeautifulSoup(reqIndividual.text, 'html.parser')

        entries = []
        entry_title = contentIndividual.find('h1')
        for entry_bib in contentIndividual.find_all('ul', {'class': 'hanging'}):
            for single_bib in entry_bib.find_all("li"):
                entries.append([entry_title.text, single_bib.text])
                print(entry_title.text, single_bib.text + "\n")
        df = pd.DataFrame(entries, columns=['Entry Title', 'Bibliography'])
        dfFixed = df.replace('\n', ' ', regex=True)
        dfFixed.to_csv('bibForAll.csv', mode='a', encoding='utf-8-sig', header=False)



















