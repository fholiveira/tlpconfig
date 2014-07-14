class PciExpressBus():
    PARAMETERS_NAME = ['PCIE_ASPM_ON_AC', 'PCIE_ASPM_ON_BAT']
    UI = 'categories/pci_express_bus.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('pci_express_bus_row')
        self.panel = loader.get('pci_express_bus_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
