class FileSystem():
    UI = 'categories/file_system.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('file_system_row')
        self.panel = loader.get('file_system_panel')
