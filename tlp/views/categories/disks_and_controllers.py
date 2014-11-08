from .category import CategoryView
from .disk import DiskOptionsView
from tlp.models import get_disks


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
