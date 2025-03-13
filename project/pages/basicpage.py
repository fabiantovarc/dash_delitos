# 📌 Importamos las librerías necesarias
import dash  # Framework principal para la creación de dashboards interactivos
from dash import html, dcc, callback, Input, Output  # Importamos componentes esenciales de Dash
import dash_bootstrap_components as dbc  # Importamos componentes de Bootstrap para el diseño

# 📌 Registramos esta página dentro de la estructura de múltiples páginas de Dash
dash.register_page(__name__)

# 📌 Importamos un componente personalizado llamado `mapsample` desde la carpeta `components/maps`
from components.maps.mapsample import mapsample

# 📌 Creamos una instancia del componente `mapsample`
# El constructor recibe dos parámetros: 
#   - Un texto personalizado que se mostrará en el mapa
#   - Un identificador único para el contenedor (`div_samplemap`)
mapa_ejemplo = mapsample('This is my custom map', 'div_samplemap')

# 📌 Definimos el layout específico de esta página
layout = dbc.Container(  # Usamos un contenedor Bootstrap para organizar la estructura de la página
    [
        dbc.Row([  # 📌 Creamos una fila dentro del contenedor
            dbc.Col([  # 📌 Agregamos una única columna que ocupará todo el ancho (lg=12)
                html.H1(['Page Title'], id="div_title_maps"),  # 📌 Agregamos un título con un ID para referencia en CSS o callbacks
                mapa_ejemplo.display()  # 📌 Llamamos al método `display()` del objeto `mapsample` para mostrar el mapa
            ], lg=12),  # 📌 La columna se extiende a lo ancho (12 de 12 columnas en Bootstrap)
        ]),
    ]
)

