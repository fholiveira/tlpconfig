from tlp.models import Group, NumericParameter, BooleanParameter


class BatteryChargeThresholdsController:

    def __init__(self):
        self.groups= [Group('CHARGE_THRESHOLDS', 
                            [NumericParameter('START_CHARGE_THRESH_BAT0'),
                             NumericParameter('STOP_CHARGE_THRESH_BAT0'),
                             NumericParameter('START_CHARGE_THRESH_BAT1'),
                             NumericParameter('STOP_CHARGE_THRESH_BAT1')])]
