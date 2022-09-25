import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.sethi3d.com.br/impressora-3d_'

headers = {
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1',
    'Connection'      : 'close'
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

dic_produto = {'Modelo':[], 'Preco':[]}

produtos = soup.find_all('div', class_=re.compile('info-produto'))
for produto in produtos:
   Modelo = produto.find(class_=re.compile('nome-produto cor-secundaria')).get_text().strip()
   Preco = produto.find('strong', class_=re.compile('cor-principal titulo')).get_text().strip()
   print(Modelo, Preco)

   dic_produto['Modelo'].append(Modelo)
   dic_produto['Preco'].append(Preco)

df = pd.DataFrame(dic_produto)
df.to_csv('C:/Users/alecs/Desktop/preco_impressora.csv', encoding='utf-8', sep=';')