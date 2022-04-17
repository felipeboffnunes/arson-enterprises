
from system.register.callbacks.main_layout import register_main_layout_callbacks
from system.register.callbacks.towers import register_towers_callbacks


def register_callbacks(app):

    app = register_main_layout_callbacks(app)
    app = register_towers_callbacks(app)

    return app
