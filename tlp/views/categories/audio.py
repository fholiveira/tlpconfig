class Audio():
    UI = 'categories/audio.ui'
    PARAMETERS_NAME = ['SOUND_POWER_SAVE_ON_AC',
                       'SOUND_POWER_SAVE_ON_BAT',
                       'SOUND_POWER_SAVE_CONTROLLER']

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('audio_row')
        self.panel = loader.get('audio_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
