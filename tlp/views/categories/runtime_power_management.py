class RuntimePowerManagement():
    UI = 'categories/runtime_power_management.ui'
    PARAMETERS_NAME = ['RUNTIME_PM_ON_AC',
                       'RUNTIME_PM_ON_BAT',
                       'RUNTIME_PM_ALL',
                       'RUNTIME_PM_BLACKLIST']

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('runtime_power_management_row')
        self.panel = loader.get('runtime_power_management_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
