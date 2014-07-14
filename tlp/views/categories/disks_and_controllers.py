class DisksAndControllers():
    UI = 'categories/disks_and_controllers.ui'
    PARAMETERS_NAME = ['DISK_DEVICES',
                       'DISK_DEVICES',
                       'DISK_APM_LEVEL_ON_AC',
                       'DISK_APM_LEVEL_ON_BAT']

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('disks_and_controllers_row')
        self.panel = loader.get('disks_and_controllers_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
