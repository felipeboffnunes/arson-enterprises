from dash import html, dcc

menu_fragment = html.Div([
    html.H1('Arson Enterprises'),
    dcc.Tabs(id='menu_fragment_tabs', value='menu_fragment_tab_1', children=[
        dcc.Tab(label='Tab 1', value='menu_fragment_tab_1'),
        dcc.Tab(label='Tab 2', value='menu_fragment_tab_2'),
        dcc.Tab(label='Tab 3', value='menu_fragment_tab_3'),
    ]),
])
