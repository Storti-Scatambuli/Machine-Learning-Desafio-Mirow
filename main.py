import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AffinityPropagation

data_countrys = pd.read_csv(r'Datas\Base de Dados - PIBs.csv')
data_countrys.drop(columns=['Classificação', 'Ano Consumido (kWh)'], inplace=True)
data_countrys = data_countrys.replace(r'^\s*$', np.nan, regex=True)
colunas_replace = ['PIB (Trilhões de Dólares)',	'Crescimento do PIB', 'Última Meta ER Revisada ', 'Custo (kWh) por USD', 'Geração de ER %']

for i in colunas_replace:
    data_countrys[i] = data_countrys[i].str.replace(',', '.').apply(pd.to_numeric)

data_countrys['Última Meta ER Revisada '] = data_countrys['Última Meta ER Revisada ']/(data_countrys['Ano Previsto da Meta ER']-2022)

paises_duvida = data_countrys[(data_countrys['Países'] == 'México') | (data_countrys['Países'] == 'França') | (data_countrys['Países'] == 'Alemanha')]

data_names_ = ['PIB (Trilhões de Dólares)', 'Crescimento do PIB',
       'Última Meta ER Revisada ', 'Ano Previsto da Meta ER',
       'Total de Emissão Fóssil de CO2 (1990)',
       'Total de Emissão Fóssil de CO2 (2000)',
       'Total de Emissão Fóssil de CO2 (2005)',
       'Total de Emissão Fóssil de CO2 (2015)',
       'Total de Emissão Fóssil de CO2 (2019)',
       'Total de Emissão Fóssil de CO2 (2020)',
       'Total de Emissão Fóssil de CO2 (2021)',
       'Total de Emissão Fóssil de CO2 (%)', 'Consumo (kWh)',
       'Custo (kWh) por USD',
       'Geração de ER %']

data_names = ['Geração de ER %','PIB (Trilhões de Dólares)',
       'Última Meta ER Revisada ', 'Custo (kWh) por USD', 'Consumo (kWh)', 'Total de Emissão Fóssil de CO2 (%)']
data = paises_duvida[data_names].values

countries = paises_duvida['Países'].tolist()
# Hierarchical Clustering

clustering = AffinityPropagation(random_state=0)
labels = clustering.fit_predict(data)

id1_name = 'PIB (Trilhões de Dólares)'
id2_name = 'Última Meta ER Revisada '

id1 = data_names.index(id1_name)
id2 = data_names.index(id2_name)

plt.figure(figsize=(10, 8))
plt.scatter(data[:, id1], data[:, id2], c=labels, cmap='viridis')
plt.xlabel(data_names[id1])
plt.ylabel(data_names[id2])
plt.title('Comparação')

# Adicionar rótulos aos países
for i, country in enumerate(countries):
    plt.annotate(country, (data[i, id1], data[i, id2]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()