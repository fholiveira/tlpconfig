from tlp import VERSION


class AboutView:
    UI = 'about.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.dialog = loader.get('about')

    def show(self, parent):
        self.dialog.set_transient_for(parent.window)
        self.dialog.set_version(VERSION)
        self.dialog.run()
        self.dialog.hide()
