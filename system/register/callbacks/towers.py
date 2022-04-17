from dash import html, Input, Output

from system.layouts.towers import towers_layout


def register_towers_callbacks(app):

    @app.callback(
        Output("towers_tabs_content", "children"),
        Input("tower_tabs", "value")
    )
    def routes_towers_tab(tab):
        return _routes_towers_tab(tab)

    return app


def _routes_towers_tab(tab: str = "DEFAULT") -> html.Div:
    tower_tabs_layout = {
        "DEFAULT": html.Div(
            html.H3("Default Tab"),
        ),
        "_TOWERS": towers_layout(),
        "REVERSE_JENGA": html.Div(
            html.H3("Reverse Jenga"),
        )
    }
    return tower_tabs_layout[tab]
