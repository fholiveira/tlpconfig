from tlp.views import Status, CategoriesGroup, load_view 
from gi.repository import Gtk


class Window():
    UI = ('window.ui', 'header.ui')

    def __init__(self, loader):
        loader.connect(self)
        self._load_childs(loader)

    def load_configuration(self, configuration):
        self.config = configuration
        self.header.set_subtitle(configuration.file_path)
    
        self.categories = CategoriesGroup(self.categories_list, self.stack)
        self.categories.render(configuration.categories)

    def save(self, button):
        print('Save!')

    def save_as(self, button):
        buttons = (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                   Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        dialog = Gtk.FileChooserDialog('Save TLP configuration file',
                                       self.window, Gtk.FileChooserAction.SAVE,
                                       buttons)

        if dialog.run() == Gtk.ResponseType.OK:
            print("File selected: " + dialog.get_filename())
    
        dialog.destroy()

    def status(self, button):
        load_view(Status).show(self.window)

    def show(self):
        self.window.present()

    def select_row(self, listbox, row):
        if row:
            self.stack.set_visible_child_name(Gtk.Buildable.get_name(row))

    def _load_childs(self, loader):
        self.panel = loader.get('panel')
        self.window = loader.get('window')
        self.categories_list = loader.get('categories')
        self.header = loader.get('header')

        self.stack = Gtk.Stack()
        self.stack.set_homogeneous(False)
        self.stack.set_visible(True)
        loader.get('category_content').add(self.stack)

        self.window.set_titlebar(self.header)
