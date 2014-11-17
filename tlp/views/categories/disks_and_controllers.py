from tlp.views.binders import ParameterBinderSelector
from .category import CategoryView
from tlp.views.binders import GroupBinder
from .disk import DiskOptionsView
from tlp.models import get_disks, Subparameter


class DisksAndControllersView(CategoryView):
    def load_controls(self, name):
        super().load_controls(name)
        self.tabs = self.loader.get('disks')
        self._load_disks_options()

    def _load_disks_options(self):
        for diskid, diskname in self.category.disks:
            tab = self.factory.create_part(DiskOptionsView)
            tab.set_header(diskname)
            self.tabs.append_page(tab.controls, tab.header)
            
            selector = ParameterBinderSelector()
            binder = lambda p: selector.get_from(p.parameters[diskid])
            selector.set_binder_by_type(Subparameter, binder)
        
            binders = [GroupBinder(selector, group) 
                       for group in self.category.disks_group]

            print (self.category.disks_group[0].parameters[0].parameters)

            for binder in binders:
                binder.bind(tab.loader)

    def create_selector(self):
        return ParameterBinderSelector()

    def groups_to_bind(self):
        return [self.category.groups[0]]
