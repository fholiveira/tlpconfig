from gi.repository import Gtk


class SystemStartAndShutdown():
    PARAMETERS_NAME = ['RESTORE_DEVICE_STATE_ON_STARTUP',
                       'DEVICES_TO_DISABLE_ON_STARTUP',
                       'DEVICES_TO_ENABLE_ON_STARTUP',
                       'DEVICES_TO_DISABLE_ON_SHUTDOWN',
                       'DEVICES_TO_ENABLE_ON_SHUTDOWN']

    UI = 'categories/system_start_and_shutdown.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.loader = loader

        self.menu = loader.get('system_start_and_shutdown_row')
        self.panel = loader.get('system_start_and_shutdown_panel')
        
        self.startup_actions = loader.get('actions_on_startup')
    
    def get_parameters(self):
        pass

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
        self.startup_actions.set_sensitive(not switch.get_active())

    def _get_devices(self, container):
        devices = [device.get_name() for device in container.get_children()
                   if not device.get_active()]

        return ' '.join(devices)
