from tlp.views import ViewLoader


class ProcessorAndFrequenceScaling():
    def __init__(self):
        loader = ViewLoader('tlp/ui/categories/processor.ui', handler=self)
        
        self.menu = loader.get('processor_row')
        self.panel = loader.get('processor_panel')
