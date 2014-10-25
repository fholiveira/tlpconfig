from . import StatusView, CategoriesStack, SavedMessageView, AboutView 
from gi.repository import Gtk


class MainView:
    UI = ('window.ui', 'header.ui', 'shell.ui')

    def __init__(self, loader, controller, factory):
        loader.connect(self)
        self.model = controller
        self.factory = factory
        self._load_ui(loader)

    def save(self, *args):
        self.model.save()
        self.factory.create_dialog(SavedMessageView).show(self)

    def save_as(self, button):
        buttons = (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                   Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        dialog = Gtk.FileChooserDialog('Save TLP configuration file',
                                       self.window, Gtk.FileChooserAction.SAVE,
                                       buttons)

        dialog.set_default_size(500, 600)

        if dialog.run() == Gtk.ResponseType.OK:
            self.model.save_as(dialog.get_filename())
            self.header.set_subtitle(self.model.configuration.file_path)
    
        dialog.destroy()

    def status(self, button):
        self.factory.create_dialog(StatusView).show(self)

    def show_about(self, *args):
        self.factory.create_dialog(AboutView).show(self)

    def show(self):
        self.categories.render(self.model.categories)

        self.model.changes.watch(lambda config: self.save_button.set_sensitive(config.has_changes()))
        self.model.changes.notify_changes()

        self.window.present()

    def _load_ui(self, loader):
        self.save_button = loader.get('save')
        self.panel = loader.get('panel')
        self.appmenu = loader.get('appmenu')
        self.window = loader.get('window')
        self.header = loader.get('header')
        self.header.set_subtitle(self.model.configuration.file_path)
        self.window.set_titlebar(self.header)
        self.categories = CategoriesStack(self.factory)
        self.categories.bind(loader.get('category_content'),
                             loader.get('categories'))
