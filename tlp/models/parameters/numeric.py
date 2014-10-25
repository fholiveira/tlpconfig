from . import Parameter


class NumericParameter(Parameter):
    @property
    def value(self):
        return float(self._value)

    @value.setter
    def value(self, value):
        self._set_value(str(value).replace('.0', ''))
