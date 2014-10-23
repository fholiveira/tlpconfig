from .category import CategoryView
from gi.repository import Gtk
from itertools import chain


class SystemStartAndShutdownView(CategoryView):
    
    def load_controls(self, name):
        super().load_controls(name)
        self.startup_actions = self.load('actions_on_startup')

    def get_groups(self):
        parameters = list(chain.from_iterable(group.parameters.values()
                                              for group in self.category.groups))
        for param, ui in parameters:
            if isinstance(ui, Gtk.Switch):
                param.value = ui.get_active()
            else:
                param.value = ' '.join([children.get_active() 
                                        for children in ui.get.children()])

    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_visible(not switch.get_active())
