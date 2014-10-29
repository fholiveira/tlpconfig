from tlp.models import Group, BooleanParameter, TextParameter


class DriveSlotUltrabayController:

    def __init__(self):
        self.groups= [Group('BAY_POWEROFF', 
                            [BooleanParameter('BAY_POWEROFF_ON_BAT')]),
                      Group('BAY_DEVICE_PANEL', 
                            [TextParameter('BAY_DEVICE', quotes='"')])]
