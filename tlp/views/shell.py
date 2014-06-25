class Shell():
    UI = ('about.ui', 'shell.ui')

    def __init__(self, loader):
        loader.connect(self)
        self.about = loader.get('about')
        self.menu = loader.get('appmenu')

    def show_about(self, action, parameter):
        self.about.run()
        self.about.hide()
