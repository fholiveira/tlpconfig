from tlp.controllers import MainController, AboutController, PreferencesController
from tlp.controllers.categories import *
from . import MainView, Builder
from .categories import *
from .dialogs import *
from tlp import UI_PATH


class ViewFactory:
    categories_path = UI_PATH + 'categories/{0}.ui'
    views_path = UI_PATH + '{0}.ui'

    def __init__(self):
        self.categories = _category_view_map()
        self.views = _view_map()

    def create_category(self, category):
        builder = Builder()
        name, view = self.categories[type(category)]
        builder.load(self.categories_path.format(name))
        return view(builder, name, category)

    def create_dialog(self, view):
        return self._create(view)

    def create(self, controller):
        return self._create(self.views[type(controller)], controller, self)

    def _create(self, view, *args):
        builder = Builder()
        if not isinstance(view.UI, tuple):
            builder.load(UI_PATH + view.UI)
            return view(builder, *args)

        for ui in view.UI:
            builder.load(UI_PATH + ui)

        return view(builder, *args)

def _view_map():
    return {MainController : MainView, 
            AboutController : AboutView,
            PreferencesController: PreferencesView}

def _category_view_map():
    return {SystemStartAndShutdownController : ('system_start_and_shutdown', SystemStartAndShutdownView),
            RuntimePowerManagementController : ('runtime_power_management', RuntimePowerManagementView),
            ProcessorAndFrequenceScalingController : ('processor_and_frequence_scaling', CategoryView),
            BatteryChargeThresholdsController : ('battery_charge_thresholds', CategoryView),
            #DisksAndControllersController : ('disks_and_controllers', CategoryView),
            #DriveSlotUltrabayController : ('drive_slot_ultrabay', CategoryView),
            UndervoltingController : ('undervolting', UndervoltingView),
            PciExpressBusController : ('pci_express_bus', CategoryView),
            GraphicsCardsController : ('graphics_cards', CategoryView),
            FileSystemController : ('file_system', CategoryView),
            NetworkingController : ('networking', CategoryView),
            KernelController : ('kernel', CategoryView),
            AudioController : ('audio', CategoryView)}
            #Usb : ('usb', CategoryView)}
