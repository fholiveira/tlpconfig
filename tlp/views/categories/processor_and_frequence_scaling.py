from .category import Category


class ProcessorAndFrequenceScaling():
    CATEGORY='PROCESSOR_AND_FREQUENCE_SCALING'

    def __init__(self, loader):
        Category.__init__(self, self.CATEGORY, loader)

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
