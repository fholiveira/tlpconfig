from .. import ChangesNotifier


class Group(ChangesNotifier):
    def __init__(self, name, parameters):
        ChangesNotifier.__init__(self)
        self.parameters = parameters
        self.name = name

    @property
    def is_active(self):
        return not any(p for p in self.parameters if not p or not p.active)
    
    @is_active.setter
    def is_active(self, value):
        for parameter in self.parameters:
            parameter.active = value
        self.notify_changes()
