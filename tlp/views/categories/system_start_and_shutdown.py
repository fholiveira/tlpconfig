from gi.repository import Gtk
from .category import Category


class SystemStartAndShutdown(Category):
    CATEGORY='SYSTEM_START_AND_SHUTDOWN'

    def __init__(self, loader):
        Category.__init__(self, self.CATEGORY, loader)
        
        self.startup_actions = self.load_control('actions_on_startup')
    
    def get_parameters(self):
        for param, ui in self.parameters.values():
            if isinstance(ui, Gtk.Switch):
                param.value = ui.get_active()
            else:
                param.value = ' '.join([children.get_active() 
                                        for children in ui.get.children()])

    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_sensitive(not switch.get_active())

    def set_parameters(self, parameters):
        self.parameters = { param.name: (param, self.loader.get(param.name))
                            for param in parameters }

        for param, ui in self.parameters.values():
            if isinstance(ui, Gtk.Switch):
                ui.set_active(param.value == '1')
            else:
                devices = param.value.split(' ')
                for children in ui.get_children():
                    children.set_active(children.get_name() in devices)

    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_visible(not switch.get_active())

    def _get_devices(self, container):
        devices = [device.get_name() for device in container.get_children()
                   if not device.get_active()]

        return ' '.join(devices)
