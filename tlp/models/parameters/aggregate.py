from . import BooleanParameter, Parameter
from .. import ChangesNotifier


class AggregateParameter(Parameter):
    def __init__(self, name, initial_value, subparametes=[], 
                 reboot_needed=False):
        Parameter.__init__(self, name, reboot_needed=reboot_needed)
        self.parameters = subparametes
        self.order = initial_value
        self._value = {}
        self.set_children(subparametes)
        
    @property
    def value(self):
        return ' '.join(self.parameters[name]._value
                        for name in self.order.values())

    @value.setter
    def value(self, value):
        self._value = {current: BooleanParameter(self.name, yes=current, no='')
                       for current in value.split() if current in self.order}

        self.notify_changes()

    def set_children(self, parameters):
        self.parameters = parameters

        for param in parameters:
            param.expand(self.order)


class Subparameter(Parameter):
    def __init__(self, template_parameter):
        Parameter.__init__(self,
                           template_parameter.name,
                           template_parameter.reboot_needed)
        self.name = template_parameter.name 
        self.template = template_parameter
        self.parameters = {}

    @property
    def value(self):
        return ' '.join(param._value for param in self.parameters.values())

    @value.setter
    def value(self, values):
        for name, value in zip(self.order, values.split()):
            param = self.parameters[name]
            param._value = value

            param.watch(lambda p: self.notify_changes())
            param.notify_changes()

    def expand(self, names):
        params = {name: self.parameters.get(name) or self.template.clone()
                  for name in names}

        self.parameters = params
        self.order = names
