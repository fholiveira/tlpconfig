from tlp.models import BooleanParameter, ParameterWatcher


class PreferencesController:
    def __init__(self, configuration):
        self.configuration = configuration

        self.parameters = self._create_parameters()
        self._load_parameters()
        self.changes = self._watch_parameters()
        
    def _create_parameters(self):
        enable_debug = '"bat disk lock nm path pm rf run sysfs udev usb"'
        self.tlp = BooleanParameter('TLP_ENABLE')

        self.trace = BooleanParameter('TLP_DEBUG', yes=enable_debug, no='""')
        self.trace.watch(self._change_active_status)

        return [self.tlp, self.trace]

    def _change_active_status(self, parameter):
        parameter.active = parameter.value

    def _load_parameters(self):
        names = [param.name for param in self.parameters]
        values = self.configuration.load_parameters(names)
        for param in self.parameters:
            param._active = True
            _, param._value = values.get(param.name, ('', ''))

    def _watch_parameters(self):
        changes = ParameterWatcher(self.parameters)
        changes.remember_state()
        return changes

    def save(self):
        self.configuration.save(self.parameters)
        self.changes.remember_state()
