import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlacion_pares(data):
    return data.corr()

def graficar_pairplot(data):
    sns.pairplot(data)
    plt.show()