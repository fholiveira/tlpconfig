from tlp.views.binders import ParameterBinderSelector


class PreferencesView:
    UI = 'preferences.ui'

    def __init__(self, loader, controller, factory):
        self.dialog = loader.get('preferences')
        self.model = controller
        loader.connect(self)

        self._set_view_behavior(loader)
        self._bind_parameters(loader)

    def show(self, parent):
        self.dialog.set_transient_for(parent.window)
        self._update_view()
        self.dialog.run()

        if self.model.changes.has_changes():
            self.model.save()
 
        self.dialog.hide()

    def _update_view(self):
        for param in self.model.parameters:
            param.notify_changes()

    def _set_view_behavior(self, loader):
        options = loader.get('TLP_OPTIONS')
        behavior = lambda switch, *a: options.set_sensitive(switch.get_active())
        loader.get('TLP_ENABLE').connect('notify::active', behavior)

    def _bind_parameters(self, loader):
        selector = ParameterBinderSelector()
        binders = [selector.get_from(param) 
                   for param in self.model.parameters]

        for binder in binders:
            binder.bind(loader.get(binder.parameter.name))

        return binders
