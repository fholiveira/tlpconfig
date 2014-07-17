from .category import Category


class DriveSlotUltrabay(Category):
    CATEGORY='DRIVE_SLOT_ULTRABAY'

    def __init__(self, loader):
        Category.__init__(self, self.CATEGORY, loader)

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
