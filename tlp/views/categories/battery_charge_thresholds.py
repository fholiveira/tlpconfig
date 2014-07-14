class BatteryChargeThresholds():
    UI = 'categories/battery_charge_thresholds.ui'
    PARAMETERS_NAME = ['START_CHARGE_THRESH_BAT0',
                       'STOP_CHARGE_THRESH_BAT0',
                       'START_CHARGE_THRESH_BAT1',
                       'STOP_CHARGE_THRESH_BAT1',
                       'DISABLE_TPACPIBAT']

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('battery_charge_thresholds_row')
        self.panel = loader.get('battery_charge_thresholds_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
