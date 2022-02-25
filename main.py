from dash import Dash
import dash_bootstrap_components as dbc

from layouts.main_page import main_page_layout

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = main_page_layout

if __name__ == '__main__':
    app.run_server(debug=True)
