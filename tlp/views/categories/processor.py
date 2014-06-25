class ProcessorAndFrequenceScaling():
    UI = 'categories/processor.ui'

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('processor_row')
        self.panel = loader.get('processor_panel')
