from . import Parameter, BooleanParameter

class DiskParameter(Parameter):
    def __init__(self, name, disks):
        Parameter.__init__(self, name)
        self.template = BooleanParameter(name)
        self.parameters = {}
        self.disks = disks
        self.name = name 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, values):
        self._set_subparameters(values[1:-1].split())

    def expand(self, names):
        params = {name: self.parameters.get(name) or self.template.clone()
                  for name in names}
        
        for disk, param in params.items():
            param.active = True
            param.yes = disk
            param.no = ''
            param.watch(lambda p: self._update_value())

        self.parameters = params
        self.order = names
    
    def initialize(self, active, value):
        self._active = active
        self.value = value

    def _update_value(self):
        value = ' '.join(param._value for param in self.parameters.values())
        self._active = any(param.value for param in self.parameters.values())
        self._value = '"{0}"'.format(value)
        self.notify_changes()

    def _set_subparameters(self, values):
        disks = (next((disk for disk in self.disks if disk.know_as(name)), None)
                 for name in values)
        self.order = [disk.id for disk in disks if disk]

        for disk, param in self.parameters.items():
            param.value = disk in self.order

        self.notify_changes()
