from tlp.models import Group, BooleanParameter


class NetworkingController:

    def __init__(self):
        self.groups= [Group('WIFI_PWR', 
                            [BooleanParameter('WIFI_PWR_ON_AC', yes='5', no='1'),
                             BooleanParameter('WIFI_PWR_ON_BAT', yes='5', no='1')]),
                      Group('WAKE_ON_LAN', 
                            [BooleanParameter('WOL_DISABLE', yes='Y', no='N')])]
