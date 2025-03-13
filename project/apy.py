# Importamos las librerías necesarias
import dash  # Importamos Dash, que es el framework principal para la creación de dashboards web
from dash import Dash, html, dcc  # Importamos componentes esenciales de Dash
import dash_bootstrap_components as dbc  # Importamos los componentes de Bootstrap para mejorar el diseño

# Variable opcional para definir un prefijo en la ruta de acceso
request_path_prefix = None

# Creamos una instancia de la aplicación Dash
# El parámetro `use_pages=True` permite usar múltiples páginas en la aplicación
# `external_stylesheets` se usa para aplicar un tema de Bootstrap (en este caso, FLATLY)
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])

# Creamos la barra de navegación en la parte superior de la aplicación
navbar = dbc.NavbarSimple([
    
    # Opción de navegación: enlace a la página de inicio
    dbc.NavItem(dbc.NavLink("Inicio", href=request_path_prefix)),
    
    # Menú desplegable con enlaces dinámicos a todas las páginas registradas
    dbc.DropdownMenu(
        [
            # Se recorren todas las páginas registradas en `dash.page_registry`
            # Se excluye la página "404 Not Found" para no mostrarla en el menú
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,  # Indica que este menú es parte de la barra de navegación
        label="Data Science",  # Nombre del menú desplegable
    ),

    # Opción de navegación: enlace a la página "Nosotros"
    dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    
    ],
    brand="Unisabana Visualización - Big Data",  # Nombre de la aplicación que aparece en la barra
    color="primary",  # Color de fondo de la barra de navegación
    dark=True,  # Indica que el texto de la barra será claro (para contrastar con el fondo oscuro)
    className="mb-2",  # Margen inferior para separar la barra de navegación del contenido
)

# Definimos la estructura principal de la aplicación
app.layout = dbc.Container(
    [
        navbar,  # Incluimos la barra de navegación
        dash.page_container  # Aquí se cargará el contenido de las páginas dinámicamente
    ],
    className="dbc",  # Clase CSS personalizada
    fluid=True,  # `fluid=True` hace que el diseño sea responsivo y ocupe toda la pantalla
)

# Se registra la aplicación de Dash en un servidor WSGI para poder ejecutarla en producción
server = app.server

# Punto de entrada principal para ejecutar la aplicación en modo local
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=True)

# - `host='0.0.0.0'` permite que la aplicación sea accesible desde otras máquinas en la red
# - `port=8050` define el puerto en el que se ejecutará la aplicación (puedes cambiarlo si es necesario)
# - `debug=True` activa el modo de depuración para ver errores en tiempo real y recargar automáticamente los cambios

