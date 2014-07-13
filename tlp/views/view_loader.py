from gi.repository import Gtk


UI_PATH = 'data/ui/'


def load_view(view):
    builder = Builder()

    if isinstance(view.UI, tuple):
        for ui in view.UI:
            builder.load(UI_PATH + ui)
    else:
        builder.load(UI_PATH + view.UI)

    return view(builder)

def create_category_loader(parameters):
    params = { param.name : param for param in parameters }

    def loader(view):
        ui = load_view(view)

        if hasattr(view, 'PARAMETERS_NAME'):
            ui.set_parameters([params[name] for name in view.PARAMETERS_NAME])
        
        return ui

    return loader


def load_css(stylesheet, screen):
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path(UI_PATH + stylesheet)

    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen,
                                    css_provider,
                                    Gtk.STYLE_PROVIDER_PRIORITY_USER)


class Builder():
    def __init__(self):
        self.builder = Gtk.Builder()

    def load(self, file):
        self.builder.add_from_file(file)

    def connect(self, handler):
        return self.builder.connect_signals(handler)

    def get(self, object_name):
        return self.builder.get_object(object_name)
