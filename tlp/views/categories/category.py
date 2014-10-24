from tlp.models import (TextParameter, BooleanParameter,
                        ListParameter, NumericParameter)
from tlp.views.binders import ParameterBinderSelector
from tlp.views.binders import GroupBinder
from gi.repository import Gtk
from itertools import chain


class CategoryView:
    def __init__(self, loader, name, category):
        loader.connect(self)

        self.category = category
        self.loader = loader
        self.load_controls(name)

        selector = self.create_selector()
        self.group_binder = [GroupBinder(selector, group) 
                             for group in category.groups]

        for binder in self.group_binder:
            binder.bind(loader)

    def create_selector(self):
        return ParameterBinderSelector()
    
    def load_controls(self, name):
        self.menu = self.loader.get(name + '_row')
        self.panel = self.loader.get(name + '_panel')

    def load(self, control_id):
        return self.loader.get(control_id)
    
    def _active_switch_changed(self, switch, parameter):
        pass

    def _set_enabled_groups(self):
        pass

    def get_parameters(self):
        return list(chain.from_iterable(group.parameters.values()
                                        for group in self.category.groups))
