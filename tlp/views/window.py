from tlp.views.categories import *
from tlp.views import ViewLoader
from gi.repository import Gtk


class Window():
    categories = [FileSystem(), ProcessorAndFrequenceScaling(), Kernel()]

    def __init__(self, app):
        self._load_childs()
        self._list_categories()
        self.window.set_titlebar(self._load_headerbar())

    def save(self, button):
        print('Save!', button)

    def show(self):
        self.window.show_all()

    def present(self):
        self.window.present()

    def select_row(self, listbox, row):
        if not row:
            return

        self.stack.set_visible_child_name(Gtk.Buildable.get_name(row))

    def _load_childs(self):
        loader = ViewLoader('tlp/ui/window.ui', handler=self)

        self.panel = loader.get('panel')
        self.window = loader.get('window')
        self.categories_list = loader.get('categories')
        self.stack = Gtk.Stack()

        loader.get('category_content').add(self.stack)

    def _load_headerbar(self):
        return ViewLoader('tlp/ui/header.ui', handler=self).get('header')

    def _list_categories(self):
        def header(row, before, user_data):
            if before and not row.get_header():
                row.set_header(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL))

        self.categories_list.set_header_func(header, None)

        for category in self.categories:
            self.categories_list.add(category.menu)
            self.stack.add_named(category.panel,
                                 Gtk.Buildable.get_name(category.menu))
