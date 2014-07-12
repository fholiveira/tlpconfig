class DriveSlotUltrabay():
    UI = 'categories/drive_slot_ultrabay.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('drive_slot_ultrabay_row')
        self.panel = loader.get('drive_slot_ultrabay_panel')
