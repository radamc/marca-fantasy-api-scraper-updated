import os
import pandas as pd

# Carpeta con XLSX
carpeta = 'data_XLSX'

# Lista de XLSX en carpeta
lista_archivos = os.listdir(carpeta)

# Inicializa DataFrame vacío
df_combinado = pd.DataFrame()

# Recorre lista y combina los datos
for archivo in lista_archivos:
    if archivo.endswith('.xlsx'):
        ruta_archivo = os.path.join(carpeta, archivo)
        df = pd.read_excel(ruta_archivo)
        # Agrega columna con el nombre del archivo (equipo)
        nombre_archivo = os.path.splitext(archivo)[0]
        df['archivo'] = nombre_archivo
        df_combinado = pd.concat([df_combinado, df])

# Reordena columna para que el equipo sea la primera columna
columnas = df_combinado.columns.tolist()
columnas = ['archivo'] + [columna for columna in columnas if columna != 'archivo']
df_combinado = df_combinado[columnas]

# Definir tabla de mapeo de reemplazo
reemplazos = {
    '13_OSA': 'OSASUNA',
    '14_RAY': 'RAYO',
    '15_RMA': 'R. MADRID',
    '162_CAD': 'CADIZ',
    '16_RSO': 'R. SOCIEDAD',
    '17_SEV': 'SEVILLA',
    '18_VAL': 'VALENCIA',
    '19_VLL': 'VALLADOLID',
    '1_ALM': 'ALMERIA',
    '20_VIL': 'VILLAREAL',
    '28_GIR': 'GIRONA',
    '2_ATM': 'ATLETI',
    '33_MLL': 'MALLORCA',
    '3_ATH': 'BILBAO',
    '4_BAR': 'BARSA',
    '5_BET': 'BETIS',
    '6_CEL': 'CELTA',
    '7_ELC': 'ELCHE',
    '8_ESP': 'ESPANYOL',
    '9_GET': 'GETAFE'
}

# Reemplazar valores en la columna "archivo" del DataFrame
df_combinado['archivo'] = df_combinado['archivo'].apply(lambda x: reemplazos.get(x, x))

df_combinado = df_combinado[['archivo', 'slug'] + [columna for columna in df_combinado.columns if columna not in ['archivo', 'slug']]]
df2 = pd.read_excel('Slug_Name.xlsx')

# Reemplaza 'ruta_del_archivo.xlsx' por la ruta del archivo de donde quieres extraer la columna NAME
df_combinado = df_combinado.merge(df2[['slug', 'NAME']], on='slug', how='left')
df_combinado = df_combinado[['archivo', 'NAME', 'slug'] + [columna for columna in df_combinado.columns if columna not in ['archivo', 'slug', 'NAME']]]

# Renombrar la columna "archivo" a "EQUIPO"
df_combinado = df_combinado.rename(columns={'archivo': 'EQUIPO'})

# Elimina columna "playerStats" no separada
df_combinado = df_combinado.drop(columns=["playerStats"])

# Reemplaza nombres redundantes
df_combinado.columns = df_combinado.columns.str.replace('marketValue.', '', regex=False)
df_combinado.columns = df_combinado.columns.str.replace('Jornada', 'J')

# Carpeta salida del data_combinado
ruta_salida = '.'

# Guarda data_combinado en carpeta salida
nombre_archivo_combinado = "data_combinado.xlsx"
ruta_archivo_combinado = os.path.join(ruta_salida, nombre_archivo_combinado)
df_combinado.to_excel(ruta_archivo_combinado, index=False)


