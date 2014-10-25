from .dialogs import StatusView, SavedMessageView, AboutView, SaveDialogView
from . import CategoriesStack


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

    def save_as(self, *args):
        dialog = SaveDialogView()
        if dialog.show(self):
            self.model.save_as(dialog.filename)

    def status(self, *args):
        self.factory.create_dialog(StatusView).show(self)

    def show_about(self, *args):
        self.factory.create(self.model.about).show(self)

    def show(self):
        self.categories.render(self.model.categories)

        self.model.changes.watch(self._on_change_config)
        self.model.changes.notify_changes()

        self.window.present()

    def _on_change_config(self, config):
        changed = config.has_changes()
        self.save_button.set_sensitive(changed)

        subtitle = self.model.configuration.file_path
        self.header.set_subtitle(subtitle if not changed else '*' + subtitle)

    def _load_ui(self, loader):
        self.save_button = loader.get('save')
        self.appmenu = loader.get('appmenu')
        self.window = loader.get('window')
        self.header = loader.get('header')
        self.panel = loader.get('panel')
        self.window.set_titlebar(self.header)
        self.categories = CategoriesStack(self.factory)
        self.categories.bind(loader.get('category_content'),
                             loader.get('categories'))
