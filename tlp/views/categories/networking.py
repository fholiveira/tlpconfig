class Networking():
    PARAMETERS_NAME = ['WIFI_PWR_ON_AC', 'WIFI_PWR_ON_BAT', 'WOL_DISABLE']
    UI = 'categories/networking.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('networking_row')
        self.panel = loader.get('networking_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
