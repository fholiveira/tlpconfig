from . import Parameter


class TextParameter(Parameter):
    def __init__(self, name, quotes='', reboot_needed=False):
        Parameter.__init__(self, name, reboot_needed=reboot_needed)
        self.quotes = quotes

    @property
    def value(self):
        return self._value.strip().replace(self.quotes, '')

    @value.setter
    def value(self, value):
        self._set_value('{0}{1}{0}'.format(self.quotes, value.strip()))

    def clone(self):
        param = TextParameter(self.name, self.quotes, self.reboot_needed)
        param._value = self._value
        return param
