class DriveSlotUltrabay():
    PARAMETERS_NAME = ['BAY_POWEROFF_ON_BAT', 'BAY_DEVICE']
    UI = 'categories/drive_slot_ultrabay.ui'


    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('drive_slot_ultrabay_row')
        self.panel = loader.get('drive_slot_ultrabay_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
