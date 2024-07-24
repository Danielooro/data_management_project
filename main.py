import pandas as pd
from exploracionDx import correlacion_pares, graficar_pairplot

# Suponiendo que tienes un dataset llamado 'data.csv'
data = pd.read_csv('data.csv')
print(correlacion_pares(data))
graficar_pairplot(data)