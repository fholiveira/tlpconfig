class SystemStartAndShutdown():
    PARAMETERS_NAME = ['RESTORE_DEVICE_STATE_ON_STARTUP',
                       'DEVICES_TO_DISABLE_ON_STARTUP',
                       'DEVICES_TO_ENABLE_ON_STARTUP',
                       'DEVICES_TO_DISABLE_ON_SHUTDOWN',
                       'DEVICES_TO_ENABLE_ON_SHUTDOWN']

    UI = 'categories/system_start_and_shutdown.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('system_start_and_shutdown_row')
        self.panel = loader.get('system_start_and_shutdown_panel')
        
        self.startup_actions = loader.get('actions_on_startup')
        
        self.startup = {'disabled' : loader.get('disable_devices_on_startup'), 
                        'enabled' : loader.get('enable_devices_on_startup')}

        self.shutdown = {'disabled' : loader.get('disable_devices_on_shutdown'), 
                         'enabled' : loader.get('enable_devices_on_shutdown')}

    def set_parameters(self, parameters):
        self.parameters = parameters


    def change_restore_devices_on_startup(self, switch, gparam):
        self.startup_actions.set_sensitive(not switch.get_active())

    def _get_devices(self, container):
        devices = [device.get_name() for device in container.get_children()
                   if not device.get_active()]

        return ' '.join(devices)

