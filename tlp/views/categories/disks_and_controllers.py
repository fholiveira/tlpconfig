from .category import CategoryView
from .disk import DiskOptionsView


class DisksAndControllersView(CategoryView):
    def load_controls(self, name):
        super().load_controls(name)
        self.tabs = self.loader.get('disks')
        self._load_disks_options()

    def _load_disks_options(self):
        for disk in ['sda - 256 GB', 'sdb - 1 TB', 'sdc - 32 GB']:
            tab = self.factory.create_part(DiskOptionsView)
            tab.set_header(disk)
            self.tabs.append_page(tab.controls, tab.header)
