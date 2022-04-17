from dash import html, Input, Output

from system.layouts.towers import towers_tabs


def register_main_layout_callbacks(app):

    @app.callback(
        Output("main-page-content", "children"),
        Input("menu_fragment_tabs", "value")
    )
    def routes_tab(tab):
        return _routes_main_tab(tab)

    return app


def _routes_main_tab(tab: str = "DEFAULT") -> html.Div:
    tabs_layout = {
        "DEFAULT": html.Div(
            html.H3("Default Tab"),
        ),
        "TOWERS": towers_tabs(),
        "CAFFEINE_CONTROL": html.Div(
            html.H3("Caffeine Control (WIP)"),
        )
    }
    return tabs_layout[tab]
