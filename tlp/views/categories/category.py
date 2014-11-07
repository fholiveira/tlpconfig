from tlp.models import (TextParameter, BooleanParameter,
                        ListParameter, NumericParameter)
from tlp.views.binders import ParameterBinderSelector
from tlp.views.binders import GroupBinder
from gi.repository import Gtk
from itertools import chain


class CategoryView:
    def __init__(self, loader, name, category, factory=None):
        loader.connect(self)

        self.category = category
        self.factory = factory
        self.loader = loader
        self.load_controls(name)
        self.bind_groups()

    def bind_groups(self):
        selector = self.create_selector()
        self.group_binder = [GroupBinder(selector, group) 
                             for group in self.category.groups]

        for binder in self.group_binder:
            binder.bind(self.loader)

    def create_selector(self):
        return ParameterBinderSelector()
    
    def load_controls(self, name):
        self.menu = self.loader.get(name + '_row')
        self.panel = self.loader.get(name + '_panel')

    def get_parameters(self):
        return list(chain.from_iterable(group.parameters.values()
                                        for group in self.category.groups))
