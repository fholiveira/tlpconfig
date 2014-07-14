class Usb():
    UI = 'categories/usb.ui'
    PARAMETERS_NAME = ['USB_AUTOSUSPEND',
                       'USB_BLACKLIST',
                       'USB_BLACKLIST_WWAN',
                       'USB_AUTOSUSPEND_DISABLE_ON_SHUTDOWN']


    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('usb_row')
        self.panel = loader.get('usb_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
