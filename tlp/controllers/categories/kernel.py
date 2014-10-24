from tlp.models import Group, BooleanParameter


class KernelController:

    def __init__(self):
        self.groups= [Group('NMI', [BooleanParameter('NMI_WATCHDOG')])]
