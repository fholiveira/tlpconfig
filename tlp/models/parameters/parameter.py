from .. import ChangesNotifier


class Parameter(ChangesNotifier):
    def __init__(self, name):
        ChangesNotifier.__init__(self)
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

    def write(self, configuration):
        old_active, old_value = self.initial_state
        template = '{0}={1}'
        old_text = template.format(self.name, old_value)
        new_text = template.format(self.name, self._value)

        if not self.active:
            new_text = '#' + new_text

        if not old_active:
            old_text = '#' + old_text
        
        return configuration.replace(old_text, new_text)

    def to_tuple(self):
        return (self._active, self._value)

    def remember_state(self):
        self.initial_state = self.to_tuple()

    def _set_value(self, new_value):
        if self._value == new_value:
            return

        self._value = new_value
        self.notify_changes()
