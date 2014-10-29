from .. import ChangesNotifier


class Parameter(ChangesNotifier):
    def __init__(self, name, reboot_needed=False):
        ChangesNotifier.__init__(self)
        self.reboot_needed = reboot_needed
        self._active = False
        self.name = name
        self._value = ''

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        if value == self._active:
            return

        self._active = value
        self.notify_changes()
    
    def to_text(self):
        return (self._textfy(self.initial_state), self._textfy(self.to_tuple()))

    def to_tuple(self):
        return (self._active, self._value)

    def remember_state(self):
        self.initial_state = self.to_tuple()

    def _textfy(self, state):
        template = '{0}={1}' if state[0] else '#{0}={1}'
        return template.format(self.name, state[1])

    def _set_value(self, new_value):
        if self._value == new_value:
            return

        self._value = new_value
        self.notify_changes()
