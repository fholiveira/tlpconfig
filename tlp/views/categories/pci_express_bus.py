class PciExpressBus():
    UI = 'categories/pci_express_bus.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('pci_express_bus_row')
        self.panel = loader.get('pci_express_bus_panel')
