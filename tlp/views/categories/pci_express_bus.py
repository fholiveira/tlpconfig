from .category import Category


class PciExpressBus(Category):
    CATEGORY='PCI_EXPRESS_BUS'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
