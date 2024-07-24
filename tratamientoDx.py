import pandas as pd

def eliminar_columnas_erroneas(data):
    return data.dropna(axis=1)

def eliminar_filas_erroneas(data):
    return data.dropna(axis=0)