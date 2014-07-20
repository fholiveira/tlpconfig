from gi.repository import Gtk
from itertools import chain
from tlp.models import (TextParameter, BooleanParameter,
                        ListParameter, NumericParameter)
from tlp.views.binders import ParameterBinderSelector


class Category:
    def __init__(self, category, loader):
        loader.connect(self)
        self.loader = loader
        self.load_controls()

        self.value_binders = ParameterBinderSelector()
    
    def load_controls(self):
        self.menu = self.loader.get('_'.join([self.CATEGORY.lower(), 'row']))
        self.panel = self.loader.get('_'.join([self.CATEGORY.lower(), 'panel']))

    @property
    def parameters(self):
        return chain.from_iterable(group.parameters.values()
                                   for group in self.groups)

    def load(self, control_id):
        return self.loader.get(control_id)
    
    def _active_switch_changed(self, switch, parameter):
        group = Gtk.Buildable.get_name(switch).replace('ACTIVE_', '')
        self.load(group).set_sensitive(switch.get_active())

    def _set_enabled_groups(self):
        for group in self.groups:
            switch = self.load('ACTIVE_' + group.name)
            switch.set_active(group.is_active)
            self._active_switch_changed(switch, None)

    def set_groups(self, groups):
        self.groups = groups
        self._set_enabled_groups()

        for parameter in self.parameters:
            self.value_binders  \
                .get_from(parameter) \
                .set_value_to(self.load(parameter.name))
