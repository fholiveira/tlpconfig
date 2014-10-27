class BooleanParameterBinder:
    def __init__(self, parameter):
        self.parameter = parameter

    def bind(self, control):
        self.control = control
        self.parameter.watch(lambda param: control.set_active(param.value))
        self.parameter.notify_changes()
        control.connect('notify::active', self._set_value)

    def _set_value(self, *args):
        self.parameter.value = self.control.get_active()
