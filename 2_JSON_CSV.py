import os
import pandas as pd
import json

# Ruta a carpeta de entrada y salida de datos
input_folder_name = 'data'
output_folder_name = 'data_CSV'

# Crear la carpeta salida si no existe
if not os.path.exists(output_folder_name):
    os.mkdir(output_folder_name)

# Ruta absoluta de carpeta principal
base_folder = os.path.abspath(os.path.dirname(__file__))
# Une ruta base con a carpetas de entrada y salida
input_folder = os.path.join(base_folder, input_folder_name)
output_folder = os.path.join(base_folder, output_folder_name)

# Recorre cada JSON en carpeta de entrada
for file_name in os.listdir(input_folder):
    # Solo procesar los archivos que tienen extensión ".json"
    if file_name.endswith('.json'):
        # Crea ruta completa del archivo
        file_path = os.path.join(input_folder, file_name)
        try:
            # Carga JSON como objeto Python
            with open(file_path, 'r') as f:
                json_data = json.load(f)
            # Normaliza datos JSON y convierte a DataFrame de Pandas
            df = pd.json_normalize(json_data)
            # Nombra CSV salida
            csv_file_name = os.path.splitext(file_name)[0] + '.csv'
            # Crea ruta completa CSV salida
            csv_file_path = os.path.join(output_folder, csv_file_name)
            # Escribe DataFrame en un CSV
            df.to_csv(csv_file_path, index=False)
        except Exception as e:
            # Imprime error si la carga del archivo JSON falla
            print(f'Error al procesar el archivo {file_name}: {e}')



