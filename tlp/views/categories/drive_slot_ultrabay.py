from .category import Category


class DriveSlotUltrabay(Category):
    CATEGORY='DRIVE_SLOT_ULTRABAY'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
