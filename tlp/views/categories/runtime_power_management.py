from ..binders import FreeTextParameterBinder
from tlp.models import TextParameter
from .category import CategoryView


class RuntimePowerManagementView(CategoryView):

    def __init__(self, loader, name, category):
        CategoryView.__init__(self, loader, name, category)
        #self.value_binders.set_binder_by_name('RUNTIME_PM_BLACKLIST', FreeTextParameterBinder)
    
    def load_controls(self, name):
        super().load_controls(name)
        self.blacklist = self.load('PM_BLACKLIST')
    
    def _devices_changed(self, combo):
        value = int(combo.get_active_id())
        self.blacklist.set_visible(not value)
