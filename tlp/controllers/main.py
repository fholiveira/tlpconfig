from itertools import chain
from .categories import *


class MainController:
    def __init__(self, configuration):
        self.configuration = configuration

        self.categories = self._create_categories()
        self._bind_configuration()

    def _bind_configuration(self):
        parameters = chain.from_iterable(group.parameters
                                         for category in self.categories
                                         for group in category.groups)
        names = [parameter.name for parameter in parameters]

        initial_values = self.configuration.load_parameters(names)
        for parameter in parameters:
            state = initial_values[parameter.name]
            parameter.initial_state = state
            parameter.value = state.get('value')
            parameter.active = state.get('active')

    def _create_categories(self):
        return [FileSystemController(), 
                ProcessorAndFrequenceScalingController(),
                KernelController(),
                UndervoltingController(),
                #DisksAndControllersController(),
                PciExpressBusController(),
                GraphicsCardsController(),
                NetworkingController(),
                AudioController(),
                #DriveSlotUltrabayController(),
                RuntimePowerManagementController(),
                #Usb(),
                SystemStartAndShutdownController(),
                BatteryChargeThresholdsController()]
