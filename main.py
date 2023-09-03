import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

data_countrys = pd.read_csv(r'Datas\Base de Dados - PIBs.csv')
data_countrys.drop(columns=['Unnamed: 1', 'Classificação'], inplace=True)
data_countrys = data_countrys.replace(r'^\s*$', np.nan, regex=True)
countrys_to_mean = ['% Share of RE Generation (excluded Hydro)', '% Share of RE Generation (including Hydro-2021)', 'Share of RE Consumption (2018)', 'Crescimento do PIB', 'Custo (kWh) por USD', 'PIB (Trilhões de Dólares)']
# countrys_no_replace = ['Crescimento do PIB', 'Custo (kWh) por USD']
countrys_to_zero = [' % Revised', '%Revised including hydro', 'Later Target', '100% renewable power target/Fossil fuel ban', 'Countries with 100% target', 'Última Meta ER Revisada ', 'Ano Previsto da Meta ER']

for i in countrys_to_mean:
    data_countrys[i] = data_countrys[i].str.replace(',', '.').apply(pd.to_numeric)
    
    col_means = data_countrys[i].mean()
    data_countrys[i] = data_countrys[i].fillna(col_means)

for i in countrys_to_zero:
    data_countrys[i] = data_countrys[i].fillna(0)


data = data_countrys[['PIB (Trilhões de Dólares)', 'Crescimento do PIB', 'Consumo (kWh)', 'Ano Consumido (kWh)', 'Custo (kWh) por USD', '% Share of RE Generation (excluded Hydro)', '% Share of RE Generation (including Hydro-2021)', 'Share of RE Consumption (2018)']].values
countries = data_countrys['Países'].tolist()
data_names = ['PIB (Trilhões de Dólares)', 'Crescimento do PIB', 'Consumo (kWh)', 'Ano Consumido (kWh)', 'Custo (kWh) por USD', '% Share of RE Generation (excluded Hydro)', '% Share of RE Generation (including Hydro-2021)', 'Share of RE Consumption (2018)']
# Hierarchical Clustering

id1 = 6
id2 = 4
clustering = AgglomerativeClustering(n_clusters=5, linkage='complete')
labels = clustering.fit_predict(data)

plt.figure(figsize=(8, 6))
plt.scatter(data[:, id1], data[:, id2], c=labels, cmap='viridis')
plt.xlabel(data_names[id1])
plt.ylabel(data_names[id2])
plt.title('Hierarchical Clustering')

# Adicionar rótulos aos países
for i, country in enumerate(countries):
    plt.annotate(country, (data[i, id1], data[i, id2]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
