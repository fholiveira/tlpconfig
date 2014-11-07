from tlp.models import Group, TextParameter


class DisksAndControllersController:

    def __init__(self):
        self.groups = [Group('SATA_LINKPWR', 
                             [TextParameter('SATA_LINKPWR_ON_BAT'),
                              TextParameter('SATA_LINKPWR_ON_AC')])]
