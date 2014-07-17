from .category import Category


class GraphicsCards(Category):
    CATEGORY='GRAPHICS_CARDS'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
