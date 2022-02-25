from dash import html
import sd_material_ui as mui

from layouts.fragments.menu import menu_fragment

main_page_layout = mui.Paper(html.Div(children=[
        menu_fragment
    ]),
)
