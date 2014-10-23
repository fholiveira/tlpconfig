class SavedMessageView():
    UI = 'save.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.dialog = loader.get('saved_message')
    
    def show(self, parent):
        self.dialog.set_transient_for(parent.window)
        self.dialog.run()

    def _button_clicked(self, button):
        self.dialog.hide()
