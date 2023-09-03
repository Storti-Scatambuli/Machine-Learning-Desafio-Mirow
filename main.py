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
