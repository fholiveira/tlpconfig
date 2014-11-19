from . import Parameter


class Subparameter(Parameter):
    def __init__(self, template, quotes=''):
        Parameter.__init__(self, template.name, template.reboot_needed)
        self.name = template.name 
        self.template = template
        self.parameters = {}
        self.quotes = quotes

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, values):
        subvalues = values.split() if not self.quotes else values[1:-1].split()
        self._set_subparameters(subvalues)
        self._update_value()

    def expand(self, names):
        params = {name: self.parameters.get(name) or self.template.clone()
                  for name in names}
        
        for param in params.values():
            param.watch(lambda p: self._update_value())

        self.parameters = params
        self.order = names
    
    def initialize(self, active, value):
        self._active = active
        self.value = value

    def _update_value(self):
        params = [self.parameters[uid] for uid in self.order]
        value = ' '.join(param._value if param.active else '_' 
                         for param in params)

        self._value = '{0}{1}{0}'.format(self.quotes, value)
        self.notify_changes()

    def _set_subparameters(self, values):
        for name, value in zip(self.order, values):
            param = self.parameters[name]
            param.active = value not in ('keep', '_')
            if param.active:
                param._value = value

            param.notify_changes()
