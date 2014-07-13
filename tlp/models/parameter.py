
class Parameter:
    def __init__(self, line):
        parameter = line.split('=')

        self.initial_state = {'active' : not line.startswith('#'),
                              'value' : parameter[1].replace('"', '')}

        self.name = parameter[0].replace('#', '')
        self.value = self.initial_state['value']

    def is_changed(self):
        return self.value != self.initial_state['value']

    def write(self, configuration)
        template = '{0}={1}'
        current = template.format(self.name, self.initial_state['value'])
        new = template.format(self.name, self.value)

        if not self.initial_value['active']:
            current = '#' + current

        return configuration.replace(current, new)
