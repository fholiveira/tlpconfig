from gi.repository import Gtk


class Category:
    def __init__(self, category, loader):
        loader.connect(self)
        self.loader = loader

        self.menu = loader.get('_'.join([category.lower(), 'row']))
        self.panel = loader.get('_'.join([category.lower(), 'panel']))

    def load_control(self, control_id):
        return self.loader.get(control_id);
    
    def _active_switch_changed(self, switch, parameter):
        group = Gtk.Buildable.get_name(switch).replace('ACTIVE_', '')
        self.load_control(group).set_sensitive(switch.get_active())

