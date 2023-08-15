# Created on Aug 15th, 2023 by Ícaro Freire (https://github.com/ivfreire)
# São Paulo, BRAZIL

import requests as r
from bs4 import BeautifulSoup
from numpy import nan
import pandas as pd


base_url = 'https://www.fundsexplorer.com.br/funds'

with open('fiis.txt', 'r') as file: fiis = file.read().split('\n')[:]
N = len(fiis)

print('Iniciando webscraping dos dados...')
print(f'baseURL = {base_url}')
print(f'FIIs listados:\t{N}')

fiis_data = {}

for i,fii in enumerate(fiis):
    try:
        url = f'{base_url}/{fii}'
        page = r.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        fiis_data[fii] = {}

        name = str(soup.find('p', class_='headerTicker__content__name').text)
        price = float(soup.find('div', class_='headerTicker__content__price').find('p').text[3:].replace('.', '').replace(',', '.'))
        
        fiis_data[fii]['Nome'] = name
        fiis_data[fii]['Preço'] = price

        indicators = soup.find_all('div', id='indicators')
        for inds in indicators:
            for box in inds.find_all('div'):
                data = box.find_all('p')
                fiis_data[fii][data[0].text] = float(data[1].text.replace(' ', '').replace('\n', '').replace('.', '').replace('R$', '').replace('%', '').replace('K', 'E3').replace('M', 'E6').replace(',', '.').replace('B', 'E9').replace('N/A', 'nan'))

        print(f'{i+1}\t{fii}\t{(i+1)*100/N:.1f}%')
    except Exception as e:
        print(f'{fii}: Exception: {e}')

fiis_df = {
    'Ticker': [],   
    'Nome': [],
    'Preço': [],
    'Liquidez Média Diária': [],
    'Último Rendimento': [],
    'Dividend Yield': [],
    'Patrimônio Líquido': [],
    'Valor Patrimonial': [],
    'Rentab. no mês': [],
    'P/VP': [],
    'Último Dividendo': [],
    'DY Últ. Dividendo': [],
    'Div. por Ação': []
}

for i,fii in enumerate(fiis_data):
    fiis_df['Ticker'].append(fii)
    for key in fiis_df.keys():
        if key != 'Ticker':
            if key in fiis_data[fii]: fiis_df[key].append(fiis_data[fii][key])
            else: fiis_df[key].append(nan)


fiis_df = pd.DataFrame(fiis_df)
fiis_df.to_csv('fiis.csv')