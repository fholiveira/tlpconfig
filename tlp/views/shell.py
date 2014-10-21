from . import About, load_view 

class Shell():
    UI = ('shell.ui')

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('appmenu')

    def show_about(self, *args):
        load_view(About).show(self.main_window)
