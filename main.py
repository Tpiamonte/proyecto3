import pandas as pd
import flask as fsk
import matplotlib.pyplot as plt


df = pd.read_csv("data_organizado.csv")

# Media
media_edad = df['Edad'].mean()
print(f"Media de Edad: {media_edad}")

# Mediana
mediana_edad = df['Edad'].median()
print(f"Mediana de Edad: {mediana_edad}")

# Desviación estándar
desviacion_edad = df['Edad'].std()
print(f"Desviación Estándar de Edad: {desviacion_edad}")

