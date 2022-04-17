
from dash import html, dcc, dash_table

from system.src.data_handler import DataHandler


def towers_tabs() -> html.Div:
    return html.Div([
        dcc.Tabs(id="tower_tabs", value="DEFAULT", children=[
            dcc.Tab(label="First Tower", value="_TOWERS"),
            dcc.Tab(label="Reverse Jenga", value="REVERSE_JENGA"),
            dcc.Tab(label="About", value="DEFAULT"),
        ]),
        html.Div(id="towers_tabs_content")]
    )


def towers_layout() -> html.Div:
    towers_data = DataHandler.get_jenga_session_dataframe()
    towers_data = towers_data.sort_values(by='Author')
    data_table = dash_table.DataTable(
            data=towers_data.to_dict('records'),
            columns=[{"name": i, "id": i} for i in ["Author", "Title", "Pages", "Review"]],
            style_cell_conditional=[
                {"if": {"column_id": "Author"}, "width": "auto"},
                {"if": {"column_id": "Title"}, "width": "auto", "textAlign": "left"},
                {"if": {"column_id": "Pages"}, "width": "10%", "textAlign": "center"},
                {"if": {"column_id": "Review"}, "width": "10%", "textAlign": "center"}
            ],
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current=0,
            page_size=20,
            css=[{'selector': '.row', 'rule': 'margin: 0'}]
    )
    return html.Div(data_table)
