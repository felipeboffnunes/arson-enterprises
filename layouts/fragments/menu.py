from dash import dcc
import dash_bootstrap_components as dbc

from layouts.fragments.logo_header import logo_header

menu_fragment = dbc.Row([
    dbc.Col(logo_header, width='auto'),
    dbc.Col(dcc.Tabs(id='menu_fragment_tabs', value='menu_fragment_tab_1', children=[
        dcc.Tab(label='Tab 1', value='menu_fragment_tab_1'),
        dcc.Tab(label='Tab 2', value='menu_fragment_tab_2'),
        dcc.Tab(label='Tab 3', value='menu_fragment_tab_3'),
    ])),
], style={'align-items': 'left', 'padding': '0'})
