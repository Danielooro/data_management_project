import pandas as pd
from tratamientoDx import eliminar_columnas_erroneas, eliminar_filas_erroneas

data = pd.read_csv('data.csv')
data = eliminar_columnas_erroneas(data)
data = eliminar_filas_erroneas(data)