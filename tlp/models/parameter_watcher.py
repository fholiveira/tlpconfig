from . import ChangesNotifier


class ParameterWatcher(ChangesNotifier):
    def __init__(self, parameters):
        ChangesNotifier.__init__(self)
        self.parameters = parameters

        for parameter in parameters:
            parameter.watch(self._parameter_changed)

    def is_changed(self):
        return not self.actual_state == self.state

    def remember_state(self):
        self.state = {param.name: param.to_tuple()
                      for param in self.parameters}
        self.actual_state = {param.name: param.to_tuple()
                             for param in self.parameters}

    def _parameter_changed(self, parameter):
        changed_before = self.is_changed()
        self.actual_state[parameter.name] = parameter.to_tuple()
        changed_after = self.is_changed()

        if (not changed_before and changed_after) or (changed_before and not changed_after):
            self.notify_changes()
