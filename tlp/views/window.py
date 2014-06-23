from tlp.views.categories import FileSystem, ProcessorAndFrequenceScaling
from gi.repository import Gtk


class Window():
    categories = [FileSystem(), ProcessorAndFrequenceScaling()]

    def __init__(self, app):
        builder = Gtk.Builder()
        builder.add_from_file('tlp/ui/window.ui')
        builder.connect_signals(self)

        self.panel = builder.get_object('panel')
        self.window = builder.get_object('window')
        self.categories_list = builder.get_object('categories')
        self.window.set_titlebar(self.get_headerbar())

    def get_headerbar(self):
        builder = Gtk.Builder()
        builder.add_from_file('tlp/ui/header.ui')
        builder.connect_signals(self)

        return builder.get_object('header')

    def save(self, button):
        print('Save!', button)

    def show(self):
        self.make_category_list()
        self.window.show_all()

    def present(self):
        self.window.present()

    def select_row(self, listbox, row):
        if not row: pass
        print('aaa')

    def make_category_list(self):
        self.categories_list.set_header_func(self.create_row_header, None)

        for category in self.categories:
            self.categories_list.add(category.menu)

    def create_row_header(self, row, before, user_data):
        if before and not row.get_header():
            row.set_header(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL))
