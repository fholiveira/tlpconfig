class RuntimePowerManagement():
    UI = 'categories/runtime_power_management.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('runtime_power_management_row')
        self.panel = loader.get('runtime_power_management_panel')
