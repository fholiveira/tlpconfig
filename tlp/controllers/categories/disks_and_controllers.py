from tlp.models import (Group, TextParameter, CompositeGroup, Subparameter,
                        NumericParameter, DiskParameter, get_disks)


class DisksAndControllersController:
    def __init__(self):
        self.disks = get_disks()
        self._create_groups()

    def _create_groups(self):
        children = {'DISK_APM_LEVEL': [Subparameter(TextParameter('DISK_APM_LEVEL_ON_AC'), quotes='"'), Subparameter(TextParameter('DISK_APM_LEVEL_ON_BAT'), quotes='"')],
                    'DISK_SPINDOWN_TIMEOUT': [Subparameter(NumericParameter('DISK_SPINDOWN_TIMEOUT_ON_AC'), quotes='"'), Subparameter(NumericParameter('DISK_SPINDOWN_TIMEOUT_ON_BAT'), quotes='"')],
                    'DISK_IOSCHED_GROUP': [Subparameter(TextParameter('DISK_IOSCHED'), quotes='"')]}

        common = [Group('SATA_LINKPWR', 
                        [TextParameter('SATA_LINKPWR_ON_BAT'),
                         TextParameter('SATA_LINKPWR_ON_AC')]),
                  CompositeGroup(DiskParameter('DISK_DEVICES', self.disks),
                                 children)]

        self.disks_groups = common[1]
        self.groups = common 
