from tlp.models import (TextParameter, BooleanParameter,
                        ListParameter, NumericParameter)
from tlp.views.binders import ParameterBinderSelector
from gi.repository import Gtk
from itertools import chain


class CategoryView:
    def __init__(self, loader, name, category):
        loader.connect(self)

        self.category = category
        self.loader = loader
        self.load_controls(name)

        self.value_binders = ParameterBinderSelector()
    
    def load_controls(self, name):
        self.menu = self.loader.get(name + '_row')
        self.panel = self.loader.get(name + '_panel')

    def load(self, control_id):
        return self.loader.get(control_id)
    
    def _active_switch_changed(self, switch, parameter):
        group_name = Gtk.Buildable.get_name(switch).replace('ACTIVE_', '')

        groups = self.category.groups
        group = [group for group in groups if group.name == group_name][0]
        group.is_active = switch.get_active()

        self.load(group_name).set_sensitive(switch.get_active())

    def _set_enabled_groups(self):
        for group in self.category.groups:
            switch = self.load('ACTIVE_' + group.name)
            switch.set_active(group.is_active)
            self._active_switch_changed(switch, None)

    def get_parameters(self):
        parameters = list(chain.from_iterable(group.parameters.values()
                                         for group in self.category.groups))
        
        for parameter in parameters:
            parameter.value = self.value_binders  \
                                  .get_from(parameter) \
                                  .get_value_from(self.load(parameter.name))

        return parameters
