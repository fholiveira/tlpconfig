class DisksAndControllers():
    UI = 'categories/disks_and_controllers.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('disks_and_controllers_row')
        self.panel = loader.get('disks_and_controllers_panel')
