class Group:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    @property
    def is_active(self):
        return not any(p for p in self.parameters.values()
                       if not p or not p.active)

class Parameter:
    def __init__(self, name,  active=False):
        self.active = active
        self.name = name
        self.value = None
        self.initial_state = {}

    @classmethod
    def from_text(cls, text):
        parameter = text.split('=')

        initial_state = {'active' : not text.startswith('#'),
                         'value' : parameter[1].replace('"', '')}

        parameter = cls(parameter[0].replace('#', ''),
                        active=initial_state['active'])

        parameter.initial_state = initial_state
        parameter.value = initial_state['value']

        return parameter

    def is_changed(self):
        start_active = self.initial_state['active']
        start_value = self.initial_state['value']
        active = self.active
        value = self.value

        return active != start_active or (active and value != start_value)

    def write(self, configuration):
        template = '{0}={1}'
        current = template.format(self.name, self.initial_state['value'])
        new = template.format(self.name, self.value)

        if not self.active:
            current = '#' + current

        return configuration.replace(current, new)
