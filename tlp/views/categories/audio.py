class Audio():
    UI = 'categories/audio.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.menu = loader.get('audio_row')
        self.panel = loader.get('audio_panel')
