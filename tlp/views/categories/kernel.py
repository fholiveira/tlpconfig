from .category import Category


class Kernel(Category):
    CATEGORY='KERNEL'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
