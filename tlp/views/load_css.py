from gi.repository import Gtk
from tlp import UI_PATH


def load_css(stylesheet, screen):
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path(UI_PATH + stylesheet)

    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen,
                                    css_provider,
                                    Gtk.STYLE_PROVIDER_PRIORITY_USER)
