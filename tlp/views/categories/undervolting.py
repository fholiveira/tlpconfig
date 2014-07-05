class Undervolting():
    UI = 'categories/undervolting.ui'

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('undervolting_row')
        self.panel = loader.get('undervolting_panel')
