from . import Parameter


class ListParameter(Parameter):
    @property
    def value(self):
        return self._value.strip().replace('"', '').split(' ')

    @value.setter
    def value(self, value):
        self._set_value('"{0}"'.format(' '.join(value)))

    def clone(self):
        param = ListParameter(self.name, self.reboot_needed)
        param._value = self._value
        return param
