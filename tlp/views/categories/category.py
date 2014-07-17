from gi.repository import Gtk


class Category:
    def __init__(self, category, configuration_groups, loader):
        loader.connect(self)
        self.loader = loader

        self.menu = loader.get('_'.join([category.lower(), 'row']))
        self.panel = loader.get('_'.join([category.lower(), 'panel']))

        self.set_parameters(configuration_groups)

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
        

    def set_parameters(self, groups):
        self.groups = groups
        self._set_enabled_groups();

    def get_parameters(self):
        pass

