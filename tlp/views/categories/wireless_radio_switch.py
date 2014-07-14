class WirelessRadioSwitch():
    UI = 'categories/wireless_radio_switch.ui'
    PARAMETERS_NAME = ['START_CHARGE_THRESH_BAT0',
                       'STOP_CHARGE_THRESH_BAT0',
                       'START_CHARGE_THRESH_BAT1',
                       'STOP_CHARGE_THRESH_BAT1',
                       'DISABLE_TPACPIBAT']

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('wireless_radio_switch_row')
        self.panel = loader.get('wireless_radio_switch_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
