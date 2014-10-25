from . import Parameter


class TextParameter(Parameter):
    def __init__(self, name, quotes=''):
        Parameter.__init__(self, name)
        self.quotes = quotes

    @property
    def value(self):
        return self._value.strip().replace(self.quotes, '')

    @value.setter
    def value(self, value):
        self._set_value('{0}{1}{0}'.format(self.quotes, value.strip()))
