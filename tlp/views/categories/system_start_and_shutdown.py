from .category import CategoryView
from gi.repository import Gtk
from itertools import chain


class SystemStartAndShutdownView(CategoryView):
    def load_controls(self, name):
        super().load_controls(name)
        self.startup_actions = self.loader.get('actions_on_startup')

    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_visible(not switch.get_active())
