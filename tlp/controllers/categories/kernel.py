from tlp.models import Group, TextParameter


class KernelController:

    def __init__(self):
        self.groups= [Group('NMI', [TextParameter('NMI_WATCHDOG')])]
