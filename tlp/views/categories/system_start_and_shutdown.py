from gi.repository import Gtk
from .category import Category
from itertools import chain


class SystemStartAndShutdown(Category):
    CATEGORY='SYSTEM_START_AND_SHUTDOWN'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
        
        self.startup_actions = self.load_control('actions_on_startup')
    
    def get_groups(self):
        for param, ui in self.parameters.values():
            if isinstance(ui, Gtk.Switch):
                param.value = ui.get_active()
            else:
                param.value = ' '.join([children.get_active() 
                                        for children in ui.get.children()])

    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_sensitive(not switch.get_active())

    def set_groups(self, groups):
        self.groups = groups
        self._set_enabled_groups();

        for param in self.parameters:
            ui = self.load_control(param.name)
            if isinstance(ui, Gtk.Switch):
                ui.set_active(param.value == '1')
            else:
                for children in ui.get_children():
                    children.set_active(children.get_name() in param.value)

    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_visible(not switch.get_active())
