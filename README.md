# Marca Fantasy Scraper
Web scraper del API de LaLiga Fantasy de Marca. Descarga la información existente en la Liga Fantasy Marca sobre los equipos y jugadores de la temporada y sus historiales de valor de mercado.
Se ha implementado multithreading (tiempo de ejecución de ~25 segundos para 1595 jugadores) y comandos varios para poder modificar la ejecución sin cambiar nada del código en caso de modificaciones o aumento de jugadores en API.

<!-- MarkdownTOC -->

- [Requisitos](#requisitos)
- [Ejecucion](#ejecucion)
- [Importado como libreria](#importado-como-libreria)
- [Funcionamiento](#funcionamiento)
- [Referencias](#referencias)
- [Implementaciones pendientes](#implementaciones-pendientes)
- [Sugerencias y Errores](#sugerencias-y-errores)

<!-- /MarkdownTOC -->


# Requisitos
- Python v3+
- Librería requests en python
- Librería numpy en python

# Ejecucion
- Descarga la última versión funcional y probada + el requirements.txt desde [releases/latest](https://github.com/alxgarci/marca-fantasy-api-scraper-updated/releases/latest)
- Para instalar el paquete requests y numpy (para los NaN), podemos hacerlo con 
```
pip install -r requirements.txt
```
- También debe instalar el paquete pandas y json

- El programa se puede ejecutar con alguno de los siguientes comandos (dependiendo de tu instalación de python):
```
python 0_SCRIPT.py
```
```
python3 0_SCRIPT.py
```
```
py 0_SCRIPT.py
```
- Ejecutará un conjunto de scripts de manera secuencial:
     · 1_Fantasy_scraper_JSON.py: con los ajustes establecidos por defecto, extrae datos creando carpetas data y players mientras muestra por pantalla un progressBar de 0% a 100%. Ejemplo de ejecución para 1595 jugadores en API por defecto (~25 segundos):

<img src="https://github.com/alxgarci/marca-fantasy-api-scraper-updated/raw/master/img/ejecucion.gif" alt="ejemplo ejecucion"/>

- Acepta algunos comandos al ejecutarlo, para más información
```
fantasy_scraper.py --help
```
<div style="text-align: center;">
<img src="https://github.com/alxgarci/marca-fantasy-api-scraper-updated/raw/master/img/ex01.png"
     alt="Ejemplo comandos"/>
</div>

     · 2_JSON_CSV.py: convierte los JSON en data a CSV creando data_CSV
     · 3_CSVplanos_XLSXlimpios.py: convierte texto de CSV plano a XSLX creando data_XLSX
     · 4_XLSXcombinado.py: unifica todos XLSX limpios libro data_combinado que se guarda en carpeta principal. Reemplaza caracteres slug por names reales

- Es importante no tener abiertos los excels generados mientras se ejecutan los scripts

# Importado como libreria
Se puede importar y usar como librería dentro de otro script:
- El _fantasy_scraper.py_ deberá encontrarse en la misma ruta que el script donde se quiere importar
- Se seguirá creando un archivo _log.txt_ en la misma ubicación que se encuentra el script
- Para actualizar los .JSON sólo se necesitan las siguientes líneas en el script desde el que se importa:
```
import fantasy_scraper
...
def main():
    ...
    fantasy_scraper.main(True, fantasy_scraper.TOTAL_JUGADORES)
    ...
...
```

# Funcionamiento
- Se creará un log.txt que registrará cada operación del programa para solución de errores
- Se almacena el .json de cada jugador en `players/IDEQUIPO_NOMBRECORTO/IDJUGADOR_NOMBRECORTO.json`
- Se crea un .json separado por cada equipo con sus jugadores y que guarda lo mismo que el jugadores pero sin estadisticas detalladas (minutos jugados,...), sólo con los puntos de cada jornada en `data/IDEQUIPO_NOMBRECORTO.json`
- En el .json de cada jugador, en la sección de `marketValue` se almacena el historial de precios de mercado (por fecha) obtenido por el api endpoint de market-values.
Ejemplo de `marketValue` en un .JSON `players/IDEQUIPO_NOMBRECORTO/IDJUGADOR_NOMBRECORTO.json`:
```
{
    ...
    "marketValue": {
            "14/07/2022": 25000000,
            "15/07/2022": 25032031,
            "16/07/2022": 24942978,
            "17/07/2022": 24668708,
            "18/07/2022": 24648333,
            "19/07/2022": 24760373,
            ...
    },
    ...
}
            
```


# Referencias
Este es un proyecto basado en el de [@diegoparrilla](https://github.com/diegoparrilla/marca-fantasy-scraper), de donde he sacado el API endpoint y parte de la estructura de los JSON.

# Implementaciones pendientes
Se pueden consultar en [issues -> labels -> mejora](https://github.com/alxgarci/marca-fantasy-api-scraper-updated/labels/mejora)

# Sugerencias y Errores
- Para errores escribir una nueva en entrada en [issues](https://github.com/alxgarci/marca-fantasy-api-scraper-updated/issues/new) subiendo el log.txt y una breve descripción del problema
- Para sugerencias escribir una nueva entrada en [issues](https://github.com/alxgarci/marca-fantasy-api-scraper-updated/issues/new)
- También revisaré los pull requests
