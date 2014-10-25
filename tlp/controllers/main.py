from tlp.controllers import AboutController
from tlp.models import ParameterWatcher
from itertools import chain
from .categories import *


class MainController:
    def __init__(self, configuration):
        self.configuration = configuration
        self.about = AboutController()
        self.categories = self._create_categories()
        self._bind_configuration()

    def save(self):
        self.configuration.save(self.changes.changed_parameters())
        self.changes.remember_state()

    def save_as(self, filename):
        self.configuration.save_as(self.changes.changed_parameters(), filename)
        self.changes.remember_state()

    def _bind_configuration(self):
        parameters = list(chain.from_iterable(group.parameters
                                              for category in self.categories
                                              for group in category.groups))

        self._set_parameters(parameters)
        self.changes = ParameterWatcher(parameters)
        self.changes.remember_state()
        
    def _set_parameters(self, parameters):
        names = [parameter.name for parameter in parameters]
        initial_values = self.configuration.load_parameters(names)
        for parameter in parameters:
            state = initial_values[parameter.name]
            parameter._value = state.get('value')
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
