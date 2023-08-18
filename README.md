# Análise de Fundos de Investimento Imobiliário

<img src='https://img.shields.io/badge/Python-green.svg'>
<img src='https://img.shields.io/badge/webscraping-green.svg'>

Fundos de Investimento Imobiliário (FIIs) são uma modalidade de investimento coletivo que têm como principal objetivo investir em ativos ligados ao mercado imobiliário, como imóveis comerciais, residenciais, shoppings, galpões industriais, entre outros. Esses fundos são formados por recursos de diversos investidores, que adquirem cotas do fundo e, assim, se tornam proprietários indiretos dos ativos imobiliários que compõem a carteira do fundo.

<img src="https://images.unsplash.com/photo-1460472178825-e5240623afd5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YnVpbGRpbmdzfGVufDB8fDB8fHww&w=1000&q=80">

Os fundos geralmente são identificados por 4 letras e o número '11' como **HGLG11** e **MXRF11**. Dentre suas propriedades, temos número de cotas, número de cotistas, patrimônio, preço, liquidez, entre outras. O objetivo deste projeto é obter estas informações sobre os fundos listados na B3 utilizando Python e *webscraping*. E então, analisar como esses parâmetros interagem entre si.

## Dados

Para obter os dados sobre os fundos, foram explorados os dados disponíveis pelo portal [fundsexplorer](https://www.fundsexplorer.com.br), que lista 400+ FIIs da bolsa de valores de São Paulo.

Os dados coletados dos fundos foram:

| Título                | Descrição     |
|-----------------------|---------------|
| Preço                 | Valor negociado pelo mercado de cada cota. |
| Liquidez Média Diária | Número de cotas compradas/vendidas por dia. |
| Último Rendimento     | Valor absoluto do último dividendo. |
| Dividend Yield        | Razão entre o preço e último rendimento. |
| Patrimônio Líquido    | Patrimônio do fundo em imóveis ou outros papéis. |
| Valor Patrimonial     | Patrimônio líquido por cota. |
| Rentab. no mês        | Valorização da cota no último mês |
| P/VP                  | Razão entre preço e valor patrimonial |
| Último Dividendo      | Último rendimento. |
| DY Últ. Dividendo     | *Dividend Yield* do último rendimento. |
| Div. por Ação         | Dividendo por cota nos último 12 meses. |
| Cotas emitidas        | Número de cotas emitidas desde o IPO. |
| Número de cotistas    | Número de pessoas/instituições que possuem cotas do fundo. |
| Segmento              | Natureza dos imóveis do fundo. |

## Referências

- https://requests.readthedocs.io/en/latest/user/quickstart/