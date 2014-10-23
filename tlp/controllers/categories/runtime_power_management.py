from tlp.models import Group, BooleanParameter, TextParameter


class RuntimePowerManagementController:

    def __init__(self):
        self.groups= [Group('RUNTIME_PM', 
                            [BooleanParameter('RUNTIME_PM_ON_AC', yes='auto', no='on'),
                             BooleanParameter('RUNTIME_PM_ON_BAT', yes='auto', no='on')]),
                      Group('RUNTIME_PM_ALL_CONFIG', 
                            [TextParameter('RUNTIME_PM_ALL')]),
                      Group('RUNTIME_PM_BLACKLIST_CONFIG', 
                            [TextParameter('RUNTIME_PM_BLACKLIST', quotes='"')])]
