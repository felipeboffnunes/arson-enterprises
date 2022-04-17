from dash import html
import dash_bootstrap_components as dbc

arson_logo = html.Img(
    src='assets/svg/Arson.svg',
    className='arson-logo',
    style={'height': '50px', 'width': '50px', 'padding-left': '10px'}
)


logo_header = dbc.Row([
    dbc.Col(arson_logo, width='auto'),
    dbc.Col(html.H4('Arson Enterprises'), style={'padding-top': '10px'}),
], style={'padding-top': '5px'})
