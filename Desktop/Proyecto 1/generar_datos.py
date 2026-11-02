import pandas as pd

# Datos de clientes
clientes_data = {
    'cliente_id': [1, 2, 3, 4],
    'nombre': ['Ana', 'Luis', 'Carlos', 'Sofia'],
    'pais': ['Argentina', 'Chile', 'Colombia', 'Mexico'],
    'fecha_registro': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05']
}

# Datos de ventas
ventas_data = {
    'venta_id': [101, 102, 103, 104, 105],
    'cliente_id': [1, 2, 1, 3, 4],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora'],
    'cantidad': [1, 2, 1, 1, 1],
    'fecha': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04', '2023-05-05']
}

# Crear DataFrames
df_clientes = pd.DataFrame(clientes_data)
df_ventas = pd.DataFrame(ventas_data)

# Guardar en CSV
df_clientes.to_csv('clientes.csv', index=False)
df_ventas.to_csv('ventas.csv', index=False)

print("Archivos clientes.csv y ventas.csv creados exitosamente.")