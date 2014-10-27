from gi.repository import Gtk
from tlp.views.categories import *


class CategoriesStack:
    def __init__(self, factory):
        self._create_stack()
        self.factory = factory

    def bind(self, panel, menu):
        panel.add(self.stack)
        self.menu = menu
        self.menu.connect('row_selected', self.switch)

    def render(self, categories):        
        self.categories = [self.factory.create_category(category) 
                           for category in categories]
    
        self._render_all()

    def switch(self, listbox, row):
        if row:
            self.stack.set_visible_child_name(Gtk.Buildable.get_name(row))

    def _create_stack(self):
        stack = Gtk.Stack()
        stack.set_homogeneous(False)
        stack.set_visible(True)
        self.stack = stack

    def _render_all(self):
        def header(row, before, user_data):
            if before and not row.get_header():
                sep = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
                row.set_header(sep)

        self.menu.set_header_func(header, None)

        for category in self.categories:
            self.menu.add(category.menu)
            self.stack.add_named(category.panel,
                                 Gtk.Buildable.get_name(category.menu))
