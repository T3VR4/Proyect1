import pandas as pd

# 1. Cargar los archivos CSV
df_clientes = pd.read_csv('clientes.csv')
df_ventas = pd.read_csv('ventas.csv')

print("--- DATOS DE CLIENTES ---")
print(df_clientes)

print("\n--- DATOS DE VENTAS ---")
print(df_ventas)

# 2. Unir ambos DataFrames usando la columna en común ('cliente_id')
df_unido = pd.merge(df_ventas, df_clientes, on='cliente_id')

print("\n--- DATOS UNIDOS (VENTAS + CLIENTES) ---")
print(df_unido)