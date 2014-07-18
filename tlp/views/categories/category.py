from gi.repository import Gtk
from itertools import chain
from tlp.models import (TextParameter, BooleanParameter,
                        ListParameter, NumericParameter)


class Category:
    def __init__(self, category, configuration_groups, loader):
        loader.connect(self)
        self.loader = loader
        self.load_controls()
        self.set_groups(configuration_groups)
    
    def load_controls(self):
        self.menu = self.loader.get('_'.join([self.CATEGORY.lower(), 'row']))
        self.panel = self.loader.get('_'.join([self.CATEGORY.lower(), 'panel']))

    def load(self, control_id):
        return self.loader.get(control_id);
    
    def _active_switch_changed(self, switch, parameter):
        group = Gtk.Buildable.get_name(switch).replace('ACTIVE_', '')
        self.load(group).set_sensitive(switch.get_active())

    def _set_enabled_groups(self):
        for group in self.groups:
            switch = self.load('ACTIVE_' + group.name)
            switch.set_active(group.is_active)
            self._active_switch_changed(switch, None);

    @property
    def parameters(self):
        return chain.from_iterable(group.parameters.values()
                                   for group in self.groups)

    def set_groups(self, groups):
        self.groups = groups
        self._set_enabled_groups()

        for parameter in self.parameters:
            self.set_control(parameter, self.load(parameter.name))

    def set_control(self, parameter, control):
        if isinstance(parameter, BooleanParameter):
            control.set_active(parameter.value)
        elif isinstance(parameter, NumericParameter):
            control.set_value(parameter.value)
        elif isinstance(parameter, TextParameter):
            if isinstance(control, Gtk.Entry):
                control.set_text(parameter.value)
            else:
                control.set_active_id(parameter.value)
        elif isinstance(parameter, ListParameter):
            for children in control.get_children():
                children.set_active(children.get_name() in parameter.value)
