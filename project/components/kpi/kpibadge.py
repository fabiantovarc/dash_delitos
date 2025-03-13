# 📌 Importamos los módulos necesarios
from dash import html  # Importamos Dash HTML para generar la estructura de la interfaz
import dash_bootstrap_components as dbc  # Importamos Bootstrap Components para mejorar el diseño

# 📌 Definimos una clase para representar un KPI con una insignia (badge)
class kpibadge:
    def __init__(self, kpi, label, badgetype):
        """
        Constructor de la clase kpibadge.

        Parámetros:
        - kpi: Valor numérico o texto que representa el KPI (Key Performance Indicator).
        - label: Descripción del KPI.
        - badgetype: Tipo de insignia (ej. "Danger" o cualquier otro valor).
        """
        self.kpi = kpi  # Guardamos el valor del KPI
        self.label = label  # Guardamos la descripción del KPI
        self.badgetype = badgetype  # Guardamos el tipo de insignia

        # 📌 Determinamos el color de la insignia según el tipo de badge
        if badgetype == 'Danger':
            self.color = "danger"  # Rojo (Bootstrap: representa alerta/peligro)
        else:
            self.color = "success"  # Verde (Bootstrap: representa éxito o positivo)

    def display(self):
        """
        Método que devuelve el layout HTML del KPI con su badge.

        Retorna:
        - Un `html.Div` con:
          - Un texto descriptivo del KPI (`label`).
          - El valor del KPI (`kpi`).
          - Una insignia (`Badge`) que indica el tipo de KPI.
        """
        layout = html.Div(
            [
                html.Div(self.label, className='h6'),  # 📌 Texto descriptivo del KPI (tamaño H6)
                html.H2(self.kpi, className='d-flex justify-content-end'),  # 📌 Valor del KPI alineado a la derecha
                dbc.Badge(self.badgetype, color=self.color, className="mr-1"),  # 📌 Badge con color según `badgetype`
            ],
            className='m-2'  # 📌 Espaciado (`m-2` = margen pequeño)
        )
        return layout  # 📌 Retornamos la estructura generada
