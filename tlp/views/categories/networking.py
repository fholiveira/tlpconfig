class Networking():
    UI = 'categories/networking.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('networking_row')
        self.panel = loader.get('networking_panel')
