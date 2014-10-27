from .dialogs import StatusView, RebootToApplyView, AboutView, SaveDialogView
from . import CategoriesStack, HomeStack


class MainView:
    UI = ('window.ui', 'editor.ui', 'welcome.ui', 'header.ui', 'shell.ui')

    def __init__(self, loader, controller, factory):
        loader.connect(self)
        self.model = controller
        self.factory = factory
        self._load_ui(loader)

    def save(self, *args):
        must_reboot = self.model.changes.need_reboot_to_apply()
        self.model.save()

        if must_reboot:
            self.factory.create_dialog(RebootToApplyView).show(self)

    def save_as(self, *args):
        dialog = SaveDialogView()
        if dialog.show(self):
            self.model.save_as(dialog.filename)

    def status(self, *args):
        self.factory.create_dialog(StatusView).show(self)

    def show_about(self, *args):
        self.factory.create(self.model.about).show(self)

    def show_preferences(self, *args):
        self.factory.create(self.model.preferences).show(self)

    def show(self):
        self.categories.render(self.model.categories)
        self._watch(self.model, self._on_change_config)
        switch = lambda *p: self.home.switch(self.model.preferences.tlp.value)
        self._watch(self.model.preferences, switch)
        self.window.present()

    def _watch(self, model, handler):
        model.changes.watch(handler)
        model.changes.notify_changes()

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

        self.home = HomeStack(loader.get('welcome'), loader.get('editor'))
        self.home.bind(self.window, [self.save_button, loader.get('save_as')])
        enable_and_save = lambda *a: self.model.preferences.enable_and_save()
        loader.get('TLP_ENABLE').connect('clicked', enable_and_save)

        self.categories = CategoriesStack(self.factory)
        self.categories.bind(loader.get('category_content'),
                             loader.get('categories'))
