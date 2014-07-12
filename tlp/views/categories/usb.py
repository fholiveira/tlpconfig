class Usb():
    UI = 'categories/usb.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('usb_row')
        self.panel = loader.get('usb_panel')
