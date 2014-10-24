from tlp.views.binders import ParameterBinderSelector
from tlp.views.binders import FreeTextParameterBinder
from tlp.models import TextParameter
from .category import CategoryView


class RuntimePowerManagementView(CategoryView):
    def create_selector(self):
        selector = ParameterBinderSelector()
        selector.set_binder_by_name('RUNTIME_PM_BLACKLIST',
                                    FreeTextParameterBinder)
        return selector
    
    def load_controls(self, name):
        super().load_controls(name)
        self.blacklist = self.loader.get('PM_BLACKLIST')
    
    def _devices_changed(self, combo):
        value = int(combo.get_active_id())
        self.blacklist.set_visible(not value)
