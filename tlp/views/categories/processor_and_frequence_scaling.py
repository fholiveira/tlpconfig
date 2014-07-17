from .category import Category


class ProcessorAndFrequenceScaling(Category):
    CATEGORY='PROCESSOR_AND_FREQUENCE_SCALING'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, configuration_groups, loader)
