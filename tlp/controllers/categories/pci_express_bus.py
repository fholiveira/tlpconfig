from tlp.models import Group, TextParameter


class PciExpressBusController:

    def __init__(self):
        self.groups= [Group('PCIE_ASPM', 
                            [TextParameter('PCIE_ASPM_ON_AC'),
                             TextParameter('PCIE_ASPM_ON_BAT')])]
