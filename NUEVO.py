import pandas as pd
import matplotlib.pyplot as plt
import os 

# No me cargaba el csv por eso tuvimos que hacer esto con ayuda del profesor
csv_file = 'clientes_electronica.csv'
if not os.path.exists(csv_file):
    print(f"Error: El archivo '{csv_file}' no se encontró. Asegúrate de que está en la misma carpeta.")
else:
    df_tienda = pd.read_csv(csv_file)
    print("DataFrame 'df_tienda' cargado exitosamente.\n")

#cargar y exportar


# Cargar el archivo CSV
df_tienda = pd.read_csv('clientes_electronica.csv')


# Mostrar las primeras 7 filas
print(df_tienda.head(7))

print("\n" + "---*" * 10 + "\n")

# Mostrar las últimas 3 filas
print(df_tienda.tail(3))

print("\n" + "---*" * 10 + "\n")

# Mostrar las columnas del DataFrame
print(df_tienda.columns)

print("\n" + "---*" * 10 + "\n")

# Mostrar la forma del DataFrame (filas, columnas)
print(df_tienda.shape)

print("\n" + "---*" * 10 + "\n")

# Resumen estadístico de columnas numéricas
print(df_tienda.describe())


print("\n" + "---*" * 20 + "\n")
print("SELECCIÓN DE COLUMNAS")
print("\n" + "---*" * 20 + "\n")


# Seleccionar columnas 'Nombre' y 'Apellido'
print(df_tienda[['Nombre', 'Apellido']])

print("\n" + "---*" * 10 + "\n")

# Seleccionar columna 'Producto Comprado'
print(df_tienda['Producto Comprado'])

print("\n" + "---*" * 20 + "\n")
print("FILTRADO DE FILAS")
print("\n" + "---*" * 20 + "\n")

# Clientes de Rosario
print(df_tienda[df_tienda['Ciudad'] == 'Rosario'])

print("\n" + "---*" * 10 + "\n")

# Productos con precio mayor a $1000
print(df_tienda[df_tienda['Precio Producto'] > 1000])

print("\n" + "---*" * 10 + "\n")

# Clientes con edad menor a 30 años
print(df_tienda[df_tienda['Edad'] < 30])

print("\n" + "---*" * 20 + "\n")
print("BLOQUE 2 | Ejercicios Intermedios de Pandas | Crear una Columna Derivada")
print("\n" + "---*" * 20 + "\n")

# Crear columna 'Venta Total'
df_tienda['Venta Total'] = df_tienda['Precio Producto'] * df_tienda['Cantidad']

print("\n" + "---*" * 10 + "\n")

# Mostrar primeras filas para verificar
print(df_tienda.head())

print("\n" + "---*" * 20 + "\n")
print("AGRUPACIONES SIMPLES")
print("\n" + "---*" * 20 + "\n")

# Suma de 'Cantidad' por 'Producto Comprado' (orden descendente)
ventas_por_producto = df_tienda.groupby('Producto Comprado')['Cantidad'].sum().sort_values(ascending=False)
print(ventas_por_producto)

print("\n" + "---*" * 10 + "\n")

# Promedio de 'Edad' por 'Ciudad'
edad_promedio_ciudad = df_tienda.groupby('Ciudad')['Edad'].mean()
print(edad_promedio_ciudad)

print("\n" + "---*" * 10 + "\n")

# 'Venta Total' por 'Ciudad' (orden descendente)
ventas_por_ciudad = df_tienda.groupby('Ciudad')['Venta Total'].sum().sort_values(ascending=False)
print(ventas_por_ciudad)

print("\n" + "---*" * 20 + "\n")
print("FILTRADO COMBINADO")
print("\n" + "---*" * 20 + "\n")

# Clientes de Mendoza que compraron más de 2 unidades
print(df_tienda[(df_tienda['Ciudad'] == 'Mendoza') & (df_tienda['Cantidad'] > 2)])

print("\n" + "---*" * 10 + "\n")

# Productos comprados en Buenos Aires por clientes mayores de 40 años
print(df_tienda[(df_tienda['Ciudad'] == 'Buenos Aires') & (df_tienda['Edad'] > 40)]['Producto Comprado'])

print("\n" + "---*" * 20 + "\n")
print("BLOQUE 3: Ejercicios de Visualización con Matplotlib")
print("\n" + "---*" * 20 + "\n")
print("VENTAS POR CIUDAD")
print("\n" + "---*" * 20 + "\n")

import matplotlib.pyplot as plt

# Datos para el gráfico
ciudades = ventas_por_ciudad.index
ventas = ventas_por_ciudad.values

# Crear gráfico
plt.bar(ciudades, ventas)
plt.title('Ventas Totales por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Venta Total ($)')
plt.xticks(rotation=45)
plt.show()

print("\n" + "---*" * 20 + "\n")
print("GRÁFICO DE BARRAS (Producto más vendido) ")
print("\n" + "---*" * 20 + "\n")

# Tomar los 5 productos más vendidos
top5_productos = ventas_por_producto.head(5)

# Crear gráfico
plt.bar(top5_productos.index, top5_productos.values)
plt.title('Top 5 Productos Más Vendidos')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.show()

print("\n" + "---*" * 20 + "\n")
print("GRÁFICO DE TORA (Clientes por ciudad)")
print("\n" + "---*" * 20 + "\n")

# Contar clientes por ciudad y tomar las 3 principales
clientes_por_ciudad = df_tienda['Ciudad'].value_counts().head(3)

# Crear gráfico de torta
plt.pie(clientes_por_ciudad, labels=clientes_por_ciudad.index, autopct='%1.1f%%')
plt.title('Distribución de Clientes por Ciudad (Top 3)')
plt.show()

print("\n" + "---*" * 20 + "\n")
print("BLOQUE 4: Ejercicio Final - Análisis Integrado")
print("\n" + "---*" * 10 + "\n")
print("Ventas por Grupo de Edad y Producto Clave")
print("\n" + "---*" * 10 + "\n")

# Crear columna 'Grupo de Edad'
bins = [0, 24, 40, 60, 100]
labels = ['Menor de 25', '25-40 años', '41-60 años', 'Mayor de 60']
df_tienda['Grupo de Edad'] = pd.cut(df_tienda['Edad'], bins=bins, labels=labels)

# Identificar los 3 productos más caros (por precio máximo)
productos_caros = df_tienda.groupby('Producto Comprado')['Precio Producto'].max().nlargest(3).index

# Filtrar datos para estos productos
df_productos_caros = df_tienda[df_tienda['Producto Comprado'].isin(productos_caros)]

# Agrupar por 'Grupo de Edad' y 'Producto Comprado'
ventas_por_edad_producto = df_productos_caros.groupby(['Grupo de Edad', 'Producto Comprado'])['Venta Total'].sum().unstack()

# Gráfico de barras agrupadas
ventas_por_edad_producto.plot(kind='bar', stacked=False)
plt.title('Ventas de Productos Caros por Grupo de Edad')
plt.xlabel('Grupo de Edad')
plt.ylabel('Venta Total ($)')
plt.xticks(rotation=45)
plt.legend(title='Producto')
plt.show()


# Análisis escrito 
print("\n" + "="*80)
print("ANÁLISIS ESCRITO: CONCLUSION")
print("="*80)
print("""
El gráfico muestra que el grupo de '41-60 años' es el que realiza mayores compras
que los demás grupos.

Posiblemente debido a diferencias en el poder adquisitivo o prioridades de consumo de estos.
""")
print("="*80)