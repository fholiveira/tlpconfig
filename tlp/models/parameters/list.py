from . import Parameter


class ListParameter(Parameter):
    @property
    def value(self):
        return self._value.strip().replace('"', '').split(' ')

    @value.setter
    def value(self, value):
        self._set_value('"{0}"'.format(' '.join(value)))
