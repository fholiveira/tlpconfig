class Kernel():
    PARAMETERS_NAME = ['NMI_WATCHDOG', 'PHC_CONTROLS']
    UI = 'categories/kernel.ui'

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('kernel_row')
        self.panel = loader.get('kernel_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
