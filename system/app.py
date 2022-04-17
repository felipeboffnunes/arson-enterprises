
import dash_bootstrap_components as dbc
from dash import Dash

from system.layouts.main_page import main_page_layout
from system.register.callback import register_callbacks

app = register_callbacks(
    Dash(
        __name__,
        title='Arson E0',
        external_stylesheets=[dbc.themes.LUX],
        suppress_callback_exceptions=True,
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        ]
    )
)
app.layout = main_page_layout
