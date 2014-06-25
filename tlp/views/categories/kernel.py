class Kernel():
    UI = 'categories/kernel.ui'

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('kernel_row')
        self.panel = loader.get('kernel_panel')
