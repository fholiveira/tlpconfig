class ProcessorAndFrequenceScaling():
    UI = 'categories/processor_and_frequence_scaling.ui'
    PARAMETERS_NAME = ['CPU_SCALING_GOVERNOR_ON_AC',
                       'CPU_SCALING_GOVERNOR_ON_BAT',
                       'CPU_SCALING_MIN_FREQ_ON_AC',
                       'CPU_SCALING_MAX_FREQ_ON_AC',
                       'CPU_SCALING_MIN_FREQ_ON_BAT',
                       'CPU_SCALING_MAX_FREQ_ON_BAT',
                       'CPU_BOOST_ON_AC',
                       'CPU_BOOST_ON_BAT',
                       'SCHED_POWERSAVE_ON_AC',
                       'SCHED_POWERSAVE_ON_BAT']

    def __init__(self, loader):
        loader.connect(self)
        
        self.menu = loader.get('processor_and_frequence_scaling_row')
        self.panel = loader.get('processor_and_frequence_scaling_panel')

    def set_parameters(self, parameters):
        pass

    def get_parameters(self):
        pass
