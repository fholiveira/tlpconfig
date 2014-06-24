from gi.repository import Gtk

class ViewLoader():
    def __init__(self, view, handler=None):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(view)

        if handler:
            self.connect(handler)

    def connect(self, handler):
        return self.builder.connect_signals(handler)

    def get(self, object_name):
        return self.builder.get_object(object_name)
    
    @staticmethod
    def load_css(file_name, screen):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(file_name)

        context = Gtk.StyleContext()
        context.add_provider_for_screen(screen,
                                        css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_USER)
