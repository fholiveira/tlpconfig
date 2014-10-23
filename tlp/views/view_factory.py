from tlp.controllers import MainController, AboutController
from tlp.views import MainView, AboutView, Builder
from tlp.controllers.categories import *
from tlp.views.categories import *
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

    def create(self, controller):
        builder = Builder()
        view = self.views[type(controller)]

        if not isinstance(view.UI, tuple):
            builder.load(UI_PATH + view.UI)
            return view(builder, controller)

        for ui in view.UI:
            builder.load(UI_PATH + ui)

        return view(builder, controller, self)


def _view_map():
    return {MainController : MainView,
            AboutController : AboutView}


def _category_view_map():
    return {FileSystemController : ('file_system', CategoryView), 
            ProcessorAndFrequenceScalingController : ('processor_and_frequence_scaling', CategoryView),
            KernelController : ('kernel', CategoryView),
            UndervoltingController : ('undervolting', UndervoltingView),
            #DisksAndControllersController : ('disks_and_controllers', CategoryView),
            PciExpressBusController : ('pci_express_bus', CategoryView),
            GraphicsCardsController : ('graphics_cards', CategoryView),
            NetworkingController : ('networking', CategoryView),
            AudioController : ('audio', CategoryView),
            #DriveSlotUltrabayController : ('drive_slot_ultrabay', CategoryView),
            RuntimePowerManagementController : ('runtime_power_management', RuntimePowerManagementView),
            #Usb : ('usb', CategoryView),
            SystemStartAndShutdownController : ('system_start_and_shutdown', SystemStartAndShutdownView),
            BatteryChargeThresholdsController : ('battery_charge_thresholds', CategoryView)}
