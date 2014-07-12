class BatteryChargeThresholds():
    UI = 'categories/battery_charge_thresholds.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('battery_charge_thresholds_row')
        self.panel = loader.get('battery_charge_thresholds_panel')
