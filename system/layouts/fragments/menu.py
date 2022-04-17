from dash import dcc
import dash_bootstrap_components as dbc

from system.layouts.fragments.logo_header import logo_header

menu_fragment = dbc.Row([
    dbc.Col(logo_header, width='auto'),
    dbc.Col(dcc.Tabs(id='menu_fragment_tabs', value='DEFAULT', children=[
        dcc.Tab(label='Reverse Jenga', value='REVERSE_JENGA'),
        dcc.Tab(label='Caffeine Control', value='CAFFEINE_CONTROL'),
        dcc.Tab(label='About', value='DEFAULT'),
    ])),
], style={'align-items': 'left', 'padding': '0'})
