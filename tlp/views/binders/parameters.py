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


class NumericParameterBinder:
    def __init__(self, parameter):
        self.parameter = parameter

    def bind(self, control):
        self.control = control
        self.parameter.watch(lambda param: control.set_value(param.value))
        self.parameter.notify_changes()
        control.connect('value-changed', self._set_value)

    def _set_value(self, *args):
        self.parameter.value = self.control.get_value()


class TextParameterBinder:
    def __init__(self, parameter):
        self.parameter = parameter

    def bind(self, control):
        self.control = control
        self.parameter.watch(lambda param: control.set_active_id(param.value))
        self.parameter.notify_changes()
        control.connect('changed', self._set_value)

    def _set_value(self, *args):
        self.parameter.value = self.control.get_active_id()


class ListParameterBinder:
    def __init__(self, parameter):
        self.parameter = parameter

    def bind(self, control):
        self.control = control
        self.parameter.watch(self._get_value)
        self.parameter.notify_changes()

        for child in self.control.get_children():
            control.connect('notify::active', self._set_value)

    def _set_value(self, parameter):
        parameter.value = [child.get_name() 
                           for child in self.control.get_children() 
                           if child.get_active()]

    def _get_value(self, *args):
        values = self.parameter.value
        for child in self.control.get_children():
            child.set_active(child.get_name() in values)
