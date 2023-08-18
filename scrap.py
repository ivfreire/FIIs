# Created on Aug 17th, 2023.
# Author: Icaro Freire. (https://github.com/ivfreire)
# São Paulo, BRAZIL.

import requests as r
from bs4 import BeautifulSoup
from numpy import nan
import pandas as pd
from datetime import datetime

base_url = 'https://www.fundsexplorer.com.br/funds'

with open('fiis.txt', 'r') as file: fiis = file.read().split('\n')
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

        infos = soup.find('div', class_='basicInformation__grid').find_all('div')
        for info in infos:
            data = info.find_all('p')
            if data[0].text == 'Segmento':
                fiis_data[fii][data[0].text] = data[1].text
            if data[0].text == 'Número de cotistas' or data[0].text == 'Cotas emitidas':
                fiis_data[fii][data[0].text] = float(data[1].text.replace('.', ''))

        print(f'{i+1}\t{fii}\t{(i+1)*100/N:.1f}%')
    except Exception as e:
        print(f'{fii}: Exception: {e}')

df_fiis = {
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
    'Div. por Ação': [],
    'Cotas emitidas': [],
    'Número de cotistas': [],
    'Segmento': []
}

for i,fii in enumerate(fiis_data):
    df_fiis['Ticker'].append(fii)
    for key in df_fiis.keys():
        if key != 'Ticker':
            if key in fiis_data[fii]: df_fiis[key].append(fiis_data[fii][key])
            else: df_fiis[key].append(nan)

df_fiis = pd.DataFrame(df_fiis)

now = datetime.now()
filename = f'FIIs-{now.year}{now.month}{now.day}-{now.hour}{now.minute}{now.second}.csv'

df_fiis.to_csv(f'data/{filename}')