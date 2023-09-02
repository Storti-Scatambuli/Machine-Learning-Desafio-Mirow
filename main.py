import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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
