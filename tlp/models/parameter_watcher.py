class ParameterWatcher:

    def __init__(self, parameters):
        self.parameters = parameters
        for parameter in parameters:
            parameter.watch(self._parameter_changed)

    def notify_group_changes(self):
        pass

    def notify_parameter_changes(self, parameter):
        pass

    def is_changed(self):
        return self.actual_state == self.state

    def remember_state():
        self.state = {parameter.name: parameter.value
                      for parameter in self.parameters}
        self.actual_state = {parameter.name: parameter.value
                             for parameter in self.parameters}

    def _parameter_changed(self, parameter):
        name = parameter.name
        value = parameter.value

        if self.actual_state[name] == value:
            return

        self.notify_parameter_changes(parameter)
        
        changed_before = self.is_changed()
        self.actual_state[name] = value
        changed_after = self.is_changed()
        if (not changed_before and changed_after) or (changed_before and not changed_after):
            self.notify_group_changes()
