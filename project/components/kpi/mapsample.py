# 📌 Importamos las librerías necesarias
from dash import html, dcc  # Componentes de Dash para la interfaz web
import plotly.express as px  # Librería para crear gráficos interactivos con Plotly

# 📌 Definimos la clase `mapsample`, que representa un mapa interactivo de elecciones de Montreal
class mapsample:    
    """ 
    Una clase para representar un mapa interactivo de elecciones de Montreal usando Dash y Plotly.
    """

    def __init__(self, map_title: str, ID: str):
        """
        Constructor de la clase `mapsample`. 
        Inicializa los atributos del mapa, como el título y el identificador único del div HTML.

        Args:
            map_title (str): Título del mapa.
            ID (str): Identificador único del contenedor `div`, usado en callbacks y CSS.
        
        Métodos:
            display()
                Genera la estructura HTML del mapa interactivo utilizando Plotly Express.

                Returns:
                    html.Div: Contenedor `Div` con un gráfico interactivo `dcc.Graph()`.
        """
        
        # 📌 Se asignan los valores a los atributos de la clase
        self.map_title = map_title  # Título que se mostrará sobre el mapa
        self.id = ID  # Identificador único del contenedor HTML del mapa

    @staticmethod
    def figura():
        """
        Método estático que genera un gráfico de mapa coroplético basado en los datos de elecciones de Montreal.

        Returns:
            fig (plotly.graph_objects.Figure): Figura de Plotly con el mapa interactivo.
        """

        # 📌 Cargamos un conjunto de datos de ejemplo proporcionado por Plotly
        df = px.data.election()  # Datos de elecciones de Montreal

        # 📌 Cargamos el archivo GeoJSON que contiene los límites geográficos de los distritos electorales
        geojson = px.data.election_geojson()

        # 📌 Creamos un mapa coroplético utilizando los datos de elecciones
        fig = px.choropleth(
            df, 
            geojson=geojson, 
            color="Bergeron",  # 📌 Se usa el color según los votos para el candidato "Bergeron"
            locations="district",  # 📌 Se vinculan los datos de los distritos con el GeoJSON
            featureidkey="properties.district",  # 📌 Se especifica la clave de los distritos en el GeoJSON
            projection="mercator"  # 📌 Usamos la proyección Mercator para el mapa
        )

        # 📌 Ajustamos el mapa para que se enfoque en los distritos sin mostrar bordes adicionales
        fig.update_geos(fitbounds="locations", visible=False)

        # 📌 Eliminamos los márgenes para que el gráfico ocupe todo el espacio disponible
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

        # 📌 Retornamos el gráfico generado
        return fig

    def display(self):
        """
        Método que genera el layout de Dash con el mapa interactivo.

        Returns:
            html.Div: Un contenedor `Div` que incluye el título y el gráfico `dcc.Graph()`.
        """

        # 📌 Creamos un contenedor `Div` que contendrá el mapa
        layout = html.Div(
            [
                # 📌 Agregamos un título con el nombre del mapa
                html.H4([self.map_title]),  

                # 📌 Contenedor interno que contiene el gráfico interactivo
                html.Div([
                    dcc.Graph(figure=self.figura())  # 📌 Se inserta la figura generada por `figura()`
                ])
                
            ], id=self.id  # 📌 Asignamos un identificador único al contenedor principal
        )

        # 📌 Retornamos la estructura HTML generada
        return layout
