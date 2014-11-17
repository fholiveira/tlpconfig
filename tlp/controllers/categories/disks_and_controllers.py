from tlp.models import (Group, TextParameter, AggregateParameter, Subparameter,
                        NumericParameter, TextParameter, get_disks)


class DisksAndControllersController:
    def __init__(self):
        self.disks = get_disks()
        self._create_groups()

    def _create_groups(self):
        common = [Group('SATA_LINKPWR', 
                        [TextParameter('SATA_LINKPWR_ON_BAT'),
                         TextParameter('SATA_LINKPWR_ON_AC')])]

        children = [Group('DISK_APM_LEVEL',
                          [Subparameter(TextParameter('DISK_APM_LEVEL_ON_AC')),
                           Subparameter(TextParameter('DISK_APM_LEVEL_ON_BAT'))]),
                    Group('DISK_SPINDOWN_TIMEOUT',
                          [Subparameter(NumericParameter('DISK_SPINDOWN_TIMEOUT_ON_AC')),
                           Subparameter(NumericParameter('DISK_SPINDOWN_TIMEOUT_ON_BAT'))]),
                    Group('DISK_IOSCHED_GROUP', 
                          [Subparameter(TextParameter('DISK_IOSCHED'))])]

        parameters = [param for group in children for param in group.parameters]

        aggregated = [Group('',
                            [AggregateParameter('DISK_DEVICES',
                                                [uid for uid, _ in self.disks],
                                                parameters)])]
         
        self.disks_group = children
        self.groups = common + aggregated + children
