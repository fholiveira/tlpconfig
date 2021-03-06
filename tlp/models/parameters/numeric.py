from . import Parameter


class NumericParameter(Parameter):
    def __init__(self, name, reboot_needed=False):
        Parameter.__init__(self, name, reboot_needed=reboot_needed)
        self._value = '0'

    @property
    def value(self):
        return float(self._value)

    @value.setter
    def value(self, value):
        self._set_value(str(value).replace('.0', ''))

    def clone(self):
        param = NumericParameter(self.name, self.reboot_needed)
        param._active = self._active
        param._value = self._value
        return param
