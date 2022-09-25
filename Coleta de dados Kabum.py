import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/escritorio/home-office/cadeira-de-escritorio'

headers = {
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1',
    'Connection'      : 'close'
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find("div", {"id": "listingCount"}).get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd)/20)

dic_produto = {'marca':[], 'preco':[]}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/escritorio/home-office/cadeira-de-escritorio?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('productCard'))
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        print(marca, preco)

        dic_produto['marca'].append(marca)
        dic_produto['preco'].append(preco)
        # print(dic_produto)
df = pd.DataFrame(dic_produto)
# df.to_csv('C:/Users/alecs/Desktop/preco_cadeira.csv', encoding='utf-8', sep=';')