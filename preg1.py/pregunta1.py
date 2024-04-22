import os
import pandas as pd

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.abspath(os.getcwd())

# Construir la ruta completa al archivo CSV
file_path = os.path.join(current_dir, 'datos', 'airbnb.csv')

# Imprimir la ruta completa para verificar
print(f'Ruta completa al archivo: {file_path}')

# Cargar el dataset
df_airbnb = pd.read_csv(file_path)

# Caso 1: Alicia busca un apartamento en Lisboa
def buscar_apartamento_alicia(df):
    # Filtra por habitaciones con más de 10 críticas y puntuación mayor a 4
    habitaciones_filtradas = df[(df['reviews'] > 10) & (df['overall_satisfaction'] > 4)]
    
    # Filtra por habitaciones que pueden acomodar a la familia de Alicia
    habitaciones_familia = habitaciones_filtradas[habitaciones_filtradas['accommodates'] >= 4]
    
    # Ordena por puntuación y número de críticas en orden descendente
    habitaciones_ordenadas = habitaciones_familia.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])
    
    # Selecciona las 3 mejores opciones
    opciones_alicia = habitaciones_ordenadas.head(3)
    
    return opciones_alicia

# Llama a la función y muestra las opciones a Alicia
opciones_alicia = buscar_apartamento_alicia(df_airbnb)
print(opciones_alicia)



