class FreeTextParameterBinder:
    def __init__(self, parameter):
        self.parameter = parameter

    def bind(self, control):
        self.control = control
        self.parameter.watch(lambda param: control.set_text(param.value))
        self.parameter.notify_changes()
        control.connect("notify::text", self._set_value)

    def _set_value(self, *args):
        self.parameter.value = self.control.get_text()
