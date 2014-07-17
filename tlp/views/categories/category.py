from gi.repository import Gtk
from itertools import chain


class Category:
    def __init__(self, category, configuration_groups, loader):
        loader.connect(self)
        self.loader = loader

        self.menu = loader.get('_'.join([category.lower(), 'row']))
        self.panel = loader.get('_'.join([category.lower(), 'panel']))

        self.set_groups(configuration_groups)

    def load_control(self, control_id):
        return self.loader.get(control_id);
    
    def _active_switch_changed(self, switch, parameter):
        group = Gtk.Buildable.get_name(switch).replace('ACTIVE_', '')
        self.load_control(group).set_sensitive(switch.get_active())

    def _set_enabled_groups(self):
        for group in self.groups:
            switch = self.load_control('ACTIVE_' + group.name)
            switch.set_active(group.is_active)
            self._active_switch_changed(switch, None);

    @property
    def parameters(self):
        return chain.from_iterable(group.parameters.values()
                                   for group in self.groups)

    def set_groups(self, groups):
        self.groups = groups
        self._set_enabled_groups()

    def get_groups(self):
        pass
