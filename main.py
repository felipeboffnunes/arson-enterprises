from dash import Dash, html

from layouts.main_page import main_page_layout

app = Dash(__name__)

app.layout = main_page_layout

if __name__ == '__main__':
    app.run_server(debug=True)
