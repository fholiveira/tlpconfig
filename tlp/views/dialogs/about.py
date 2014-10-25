class AboutView:
    UI = 'about.ui'

    def __init__(self, loader, controller, factory):
        self.dialog = loader.get('about')
        self.model = controller
        loader.connect(self)

    def show(self, parent):
        self.dialog.set_transient_for(parent.window)
        self.dialog.set_version(self.model.version)
        self.dialog.run()
        self.dialog.hide()
