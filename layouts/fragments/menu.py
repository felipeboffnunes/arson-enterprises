from dash import html, dcc
import dash_bootstrap_components as dbc

menu_fragment = dbc.Row([
    dbc.Col(html.P('Arson Enterprises'), width=2),
    dbc.Col(dcc.Tabs(id='menu_fragment_tabs', value='menu_fragment_tab_1', children=[
        dcc.Tab(label='Tab 1', value='menu_fragment_tab_1'),
        dcc.Tab(label='Tab 2', value='menu_fragment_tab_2'),
        dcc.Tab(label='Tab 3', value='menu_fragment_tab_3'),
    ]), width=10, style={'width': '100%'}),
], style={'display': 'flex'})
