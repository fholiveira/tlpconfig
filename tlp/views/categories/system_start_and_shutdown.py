class SystemStartAndShutdown():
    UI = 'categories/system_start_and_shutdown.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('system_start_and_shutdown_row')
        self.panel = loader.get('system_start_and_shutdown_panel')
