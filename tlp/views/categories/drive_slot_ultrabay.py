from tlp.views.binders import ParameterBinderSelector
from tlp.views.binders import FreeTextParameterBinder
from tlp.models import TextParameter
from .category import CategoryView


class DriveSlotUltrabayView(CategoryView):
    def create_selector(self):
        selector = ParameterBinderSelector()
        selector.set_binder_by_type(TextParameter, FreeTextParameterBinder)
        return selector

    def load_controls(self, name):
        super().load_controls(name)
        self.driver_panel = self.loader.get('BAY_DEVICE_BOX')
        self.driver_panel.set_visible(False)
    
    def _change_driver_power_state(self, switch, *args):
        value = switch.get_active()
        self.driver_panel.set_visible(value)
