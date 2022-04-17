from dash import dcc
import dash_bootstrap_components as dbc

from system.layouts.fragments.logo_header import logo_header

menu_fragment = dbc.Row([
    dbc.Col(logo_header, width='auto'),
    dbc.Col(dcc.Tabs(id='menu_fragment_tabs', value='menu_fragment_tab_1', children=[
        dcc.Tab(label='Reverse Jenga', value='menu_fragment_tab_1'),
        dcc.Tab(label='Caffeine Control', value='menu_fragment_tab_2'),
        dcc.Tab(label='About', value='menu_fragment_tab_3'),
    ])),
], style={'align-items': 'left', 'padding': '0'})
