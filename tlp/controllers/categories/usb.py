from tlp.models import Group, BooleanParameter, TextParameter


class UsbController:
    def __init__(self):
        self.groups= [Group('USB_AUTOSUSPEND_GROUP', 
                            [BooleanParameter('USB_AUTOSUSPEND')]),
                      Group('USB_BLACKLIST_GROUP', 
                            [TextParameter('USB_BLACKLIST', quotes='"'),
                             BooleanParameter('USB_BLACKLIST_WWAN')]),
                      Group('USB_AUTOSUSPEND_DISABLE_ON_SHUTDOWN_GROUP', 
                            [BooleanParameter('USB_AUTOSUSPEND_DISABLE_ON_SHUTDOWN')])]
