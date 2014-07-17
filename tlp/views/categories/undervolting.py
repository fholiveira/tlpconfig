from .category import Category


class Undervolting(Category):
    CATEGORY='UNDERVOLTING'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
