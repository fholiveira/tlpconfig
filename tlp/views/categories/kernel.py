from tlp.views import ViewLoader


class Kernel():
    def __init__(self):
        loader = ViewLoader('tlp/ui/categories/kernel.ui', handler=self)
        
        self.menu = loader.get('kernel_row')
        self.panel = loader.get('kernel_panel')
