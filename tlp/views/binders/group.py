class GroupBinder:
    def __init__(self, selector, group):
        self.selector = selector
        self.group = group

    def bind(self, loader):
        self.panel = loader.get(self.group.name)
        self.panel.set_sensitive(self.group.is_active)
        self.switch = loader.get('ACTIVE_' + self.group.name)
        self.switch.connect("notify::active", self._change_enabled)

        self.group.watch(lambda group: self.switch.set_active(group.is_active))
        self.group.notify_changes()        

        self.parameters_binders = self._bind_parameters(loader)

    def _change_enabled(self, *args):
        active = self.switch.get_active()
        self.group.is_active = active
        self.panel.set_sensitive(active)

    def _bind_parameters(self, loader):
        binders = [self.selector.get_from(param) 
                   for param in self.group.parameters]

        for binder in binders:
            binder.bind(loader.get(binder.parameter.name))

        return binders
