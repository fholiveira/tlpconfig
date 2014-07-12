class ProcessorAndFrequenceScaling():
    UI = 'categories/processor_and_frequence_scaling.ui'

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('processor_and_frequence_scaling_row')
        self.panel = loader.get('processor_and_frequence_scaling_panel')
