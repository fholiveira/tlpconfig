class GraphicsCards():
    UI = 'categories/graphics_cards.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('graphics_cards_row')
        self.panel = loader.get('graphics_cards_panel')
