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
