from . import Parameter


class BooleanParameter(Parameter):
    def __init__(self, name, yes='1', no='0', reboot_needed=False):
        Parameter.__init__(self, name, reboot_needed=reboot_needed)
        self.yes = yes
        self.no = no
        self._value = no

    @property
    def value(self):
        return self._value.strip() == self.yes

    @value.setter
    def value(self, value):
        self._set_value(self.yes if value else self.no)
