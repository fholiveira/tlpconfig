from .category import CategoryView
from tlp.views.binders import GroupBinder
from .disk import DiskOptionsView
from tlp.models import get_disks, Subparameter, Group


class DisksAndControllersView(CategoryView):
    def load_controls(self, name):
        super().load_controls(name)
        self.tabs = self.loader.get('disks')
        self._load_disks_options()

    def _load_disks_options(self):
        groups = self.category.disks_groups.subgroups()
        head = self.category.disks_groups.head 
        for disk in self.category.disks:
            tab = self.factory.create_part(DiskOptionsView)
            tab.set_header(disk.alias + " - " + disk.size)
            tab.bind_groups(head.parameters[disk.id], groups[disk.id])

            self.tabs.append_page(tab.controls, tab.header)

    def groups_to_bind(self):
        return [group
                for group in self.category.groups
                if isinstance(group, Group)]
