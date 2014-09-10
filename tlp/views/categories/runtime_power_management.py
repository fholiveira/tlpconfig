from ..binders import FreeTextParameterBinder
from ...models import TextParameter
from .category import Category


class RuntimePowerManagement(Category):
    CATEGORY='RUNTIME_POWER_MANAGEMENT'

    def __init__(self, loader, configuration_groups):
        Category.__init__(self, self.CATEGORY, loader)

        self.value_binders.set_binder_by_name('RUNTIME_PM_BLACKLIST', FreeTextParameterBinder)

        self.set_groups(configuration_groups)
    
    def load_controls(self):
        super().load_controls()
        self.blacklist = self.load('PM_BLACKLIST')
    
    def _devices_changed(self, combo):
        value = int(combo.get_active_id())
        self.blacklist.set_visible(not value)
