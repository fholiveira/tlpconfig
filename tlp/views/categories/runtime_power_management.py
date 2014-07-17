from .category import Category


class RuntimePowerManagement(Category):
    CATEGORY='RUNTIME_POWER_MANAGEMENT'

    def __init__(self, loader):
        Category.__init__(self, self.CATEGORY, loader)

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
