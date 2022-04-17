from dash import html, Input, Output


def register_callbacks(app):

    @app.callback(
        Output("main-page-content", "children"),
        Input("menu_fragment_tabs", "value")
    )
    def routes_tab(tab):
        return _routes_tab(tab)

    return app


def _routes_tab(tab: str = "DEFAULT") -> html.Div:
    tabs_layout = {
        "DEFAULT": html.Div(
            html.H3("Default Tab"),
        ),
        "REVERSE_JENGA": html.Div(
            html.H3("Reverse Jenga"),
        ),
        "CAFFEINE_CONTROL": html.Div(
            html.H3("Caffeine Control"),
        )
    }
    return tabs_layout[tab]
