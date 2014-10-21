from tlp.models import (BooleanParameter, ListParameter,
                        NumericParameter, TextParameter)
from .default_binders import (BooleanParameterBinder, ListParameterBinder,
                              NumericParameterBinder, TextParameterBinder )


class ParameterBinderSelector:
    def __init__(self):
        self.binders_by_name = {}
        self.binders_by_type = {BooleanParameter: BooleanParameterBinder,
                                ListParameter: ListParameterBinder,
                                NumericParameter: NumericParameterBinder,
                                TextParameter: TextParameterBinder}

    def get_from(self, parameter):
        binder = self.binders_by_name.get(parameter.name,
                                          self.binders_by_type[type(parameter)])
        return binder(parameter)

    def set_binder_by_type(self, parameter_type, binder_type):
        self.binders_by_type[parameter_type] = binder_type

    def set_binder_by_name(self, parameter_name, binder_type):
        self.binders_by_name[parameter_name] = binder_type
