from tlp.models import Group, BooleanParameter, ListParameter


class SystemStartAndShutdownController:

    def __init__(self):
        self.groups= [Group('DEVICE_STATE', 
                            [BooleanParameter('RESTORE_DEVICE_STATE_ON_STARTUP')]),
                      Group('DISABLE_ON_STARTUP', 
                            [ListParameter('DEVICES_TO_DISABLE_ON_STARTUP')]),
                      Group('ENABLE_ON_STARTUP', 
                            [ListParameter('DEVICES_TO_ENABLE_ON_STARTUP')]),
                      Group('DISABLE_ON_SHUTDOWN', 
                            [ListParameter('DEVICES_TO_DISABLE_ON_SHUTDOWN')]),
                      Group('ENABLE_ON_SHUTDOWN', 
                            [ListParameter('DEVICES_TO_ENABLE_ON_SHUTDOWN')])]
