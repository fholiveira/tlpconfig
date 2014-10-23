from tlp.models import Group, NumericParameter


class FileSystemController:

    def __init__(self):
        self.groups= [Group('DISK_IDLE_SECS', 
                            [NumericParameter('DISK_IDLE_SECS_ON_AC'),
                             NumericParameter('DISK_IDLE_SECS_ON_BAT')]),
                      Group('MAX_LOST_WORK_SECS', 
                            [NumericParameter('MAX_LOST_WORK_SECS_ON_AC'),
                             NumericParameter('MAX_LOST_WORK_SECS_ON_BAT')])]
