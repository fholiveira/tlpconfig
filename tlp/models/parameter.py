class Parameter:
    def __init__(self, name):
        self.changes_handlers = []
        self.initial_state = {}
        self._active = False
        self._value = ''
        self.name = name

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        if value == self._active:
            return
        self._active = value
        self.notify_changes()

    def is_changed(self):
        start_active = self.initial_state['active']
        start_value = self.initial_state['value']
        active = self.active
        value = self._value

        return active != start_active or (active and value != start_value)

    def write(self, configuration):
        template = '{0}={1}'
        current = template.format(self.name, self.initial_state['value'])
        new = template.format(self.name, self._value)

        if not self.active:
            new = '#' + new

        if not self.initial_state['active']:
            current = '#' + current
        
        return configuration.replace(current, new)
 
    def watch(self, handler):
        self.changes_handlers.append(handler)

    def notify_changes(self):
        for handler in self.changes_handlers:
            handler(self)

    def _set_value(self, new_value):
        if self._value == new_value:
            return

        self._value = new_value
        self.notify_changes()


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


class ListParameter(Parameter):
    @property
    def value(self):
        return self._value.strip().replace('"', '').split(' ')

    @value.setter
    def value(self, value):
        self._set_value('"{0}"'.format(' '.join(value)))


class BooleanParameter(Parameter):
    def __init__(self, name, yes='1', no='0'):
        Parameter.__init__(self, name)
        self.yes = yes
        self.no = no

    @property
    def value(self):
        return self._value.strip() == self.yes

    @value.setter
    def value(self, value):
        self._set_value(self.yes if value else self.no)


class NumericParameter(Parameter):
    @property
    def value(self):
        return float(self._value)

    @value.setter
    def value(self, value):
        self._set_value(str(value).replace('.0', ''))
