from tlp.models import Group, TextParameter, get_disks


class DisksAndControllersController:

    def __init__(self):
        self.groups = [Group('SATA_LINKPWR', 
                             [TextParameter('SATA_LINKPWR_ON_BAT'),
                              TextParameter('SATA_LINKPWR_ON_AC')])]

        self.disks = get_disks()
