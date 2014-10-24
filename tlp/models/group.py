class Group:
    def __init__(self, name, parameters):
        self.changes_handlers = []
        self.name = name
        self.parameters = parameters

    @property
    def is_active(self):
        return not any(p for p in self.parameters
                       if not p or not p.active)
    
    @is_active.setter
    def is_active(self, value):
        for parameter in self.parameters:
            parameter.active = value

    def watch(self, handler):
        self.changes_handlers.append(handler)

    def notify_changes(self):
        for handler in self.changes_handlers:
            handler(self)
