from tlp.models import ChangesNotifier


class ParameterWatcher(ChangesNotifier):
    def __init__(self, parameters):
        ChangesNotifier.__init__(self)
        self.parameters = parameters

        for parameter in parameters:
            parameter.watch(self._parameter_changed)

    def has_changes(self):
        return not self.actual_state == self.state

    def changed_parameters(self):
        return [param for param in self.parameters if self._is_changed(param)]

    def need_reboot_to_apply(self):
        return any(param for param in self.parameters 
                   if param.reboot_needed and self._is_changed(param))

    def _is_changed(self, param):
        return self.state[param.name] != self.actual_state[param.name]

    def remember_state(self):
        self.actual_state = self._take_state_snapshot()
        self.state = self._take_state_snapshot()

        for parameter in self.parameters:
            parameter.remember_state()

        self.notify_changes()

    def _take_state_snapshot(self):
        return {param.name: param.to_tuple() for param in self.parameters}

    def _parameter_changed(self, parameter):
        changed_before = self.has_changes()
        self.actual_state[parameter.name] = parameter.to_tuple()
        changed_after = self.has_changes()
        
        if (not changed_before and changed_after) or (changed_before and not changed_after):
            self.notify_changes()
