import os
import pandas as pd

#Bucle 1: crea XLSX y separa valores "externos" 
# Ruta principal
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Ruta a carpeta entrada
carpeta_csv = os.path.join(ruta_script, 'data_CSV')

# Ruta a carpeta salida
carpeta_excel = os.path.join(ruta_script, 'data_XLSX')

# Crear la carpeta salida si no existe
if not os.path.exists(carpeta_excel):
    os.mkdir(carpeta_excel)

# Lista de CSV en carpeta entrada
archivos_csv = os.listdir(carpeta_csv)

# Recorre cada CSV y crea un XLSX para cada uno
for archivo in archivos_csv:
    if archivo.endswith('.csv'):
        # Lee el CSV
        ruta_csv = os.path.join(carpeta_csv, archivo)
        df = pd.read_csv(ruta_csv)
        
        # Crea un XLSX y escribe datos separados en hoja 'datos'
        ruta_xlsx = os.path.join(carpeta_excel, archivo.replace('.csv', '.xlsx'))
        with pd.ExcelWriter(ruta_xlsx) as writer:
            df.to_excel(writer, sheet_name='datos', index=False)

#Bucle 2: Separa valores "internos" en cada XLSX
# Obtiene la ruta de carpeta salida
ruta_carpeta = carpeta_excel

# Lista de XLSX en carpeta salida
archivos_excel = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.endswith('.xlsx')]

# Recorre y modifica cada XLSX
for archivo in archivos_excel:
    # Carga XLSX en DataFrame de Pandas
    df = pd.read_excel(os.path.join(ruta_carpeta, archivo))
    
    # Mueve columna 'playerStats' al final y elimina corchetes
    df['playerStats'] = df.pop('playerStats').apply(lambda x: str(x).strip('[]'))
    
    # Reemplaza valores 'nan' por vacios
    df['playerStats'] = df['playerStats'].apply(lambda x: x.replace('nan', ''))
    
    # Separa el texto de columna 'playerStats' en varias columnas
    df[['Jornada'+str(i) for i in range(1, 39)]] = df['playerStats'].str.split(',', expand=True)
    
    # Sobrescribe XLSX
    df.to_excel(os.path.join(ruta_carpeta, archivo), index=False)


