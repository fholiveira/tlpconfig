from tlp.views import ViewLoader


class FileSystem():
    def __init__(self):
        loader = ViewLoader('tlp/ui/categories/file_system.ui', handler=self)
        
        self.menu = loader.get('file_system_row')
        self.panel = loader.get('file_system_panel')
