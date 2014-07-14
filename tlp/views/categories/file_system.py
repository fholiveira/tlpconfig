class FileSystem():
    UI = 'categories/file_system.ui'
    PARAMETERS_NAME = ['DISK_IDLE_SECS_ON_AC',
                       'DISK_IDLE_SECS_ON_BAT',
                       'MAX_LOST_WORK_SECS_ON_AC',
                       'MAX_LOST_WORK_SECS_ON_BAT']

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('file_system_row')
        self.panel = loader.get('file_system_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
