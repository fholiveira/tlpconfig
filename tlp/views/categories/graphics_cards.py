class GraphicsCards():
    UI = 'categories/graphics_cards.ui'
    PARAMETERS_NAME = ['RADEON_POWER_PROFILE_ON_AC',
                       'RADEON_POWER_PROFILE_ON_BAT',
                       'RADEON_DPM_STATE_ON_AC',
                       'RADEON_DPM_STATE_ON_BAT',
                       'RADEON_DPM_PERF_LEVEL_ON_AC',
                       'RADEON_DPM_PERF_LEVEL_ON_BAT'] 

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('graphics_cards_row')
        self.panel = loader.get('graphics_cards_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
