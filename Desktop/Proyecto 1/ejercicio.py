import pandas as pd

# 1. Cargar y unir los datos (como hicimos antes)
df_clientes = pd.read_csv('clientes.csv')
df_ventas = pd.read_csv('ventas.csv')
df_unido = pd.merge(df_ventas, df_clientes, on='cliente_id')

print("--- DATOS COMPLETOS ---")
print(df_unido)

# 2. FILTRAR: Mostrar solo las ventas donde la cantidad sea mayor a 1
print("\n--- FILTRO: Ventas con cantidad > 1 ---")
ventas_filtradas = df_unido[df_unido['cantidad'] > 1]
print(ventas_filtradas[['nombre', 'producto', 'cantidad', 'pais']])

# 3. AGRUPAR: Sumar la cantidad de productos vendidos por país
print("\n--- AGRUPACIÓN: Total de productos vendidos por país ---")
ventas_por_pais = df_unido.groupby('pais')['cantidad'].sum().reset_index()
print(ventas_por_pais)