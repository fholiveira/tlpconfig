class Undervolting():
    UI = 'categories/undervolting.ui'
    PARAMETERS_NAME = ['PHC_CONTROLS']

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('undervolting_row')
        self.panel = loader.get('undervolting_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
