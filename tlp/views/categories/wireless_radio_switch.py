class WirelessRadioSwitch():
    UI = 'categories/wireless_radio_switch.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('wireless_radio_switch_row')
        self.panel = loader.get('wireless_radio_switch_panel')
