class RebootToApplyView():
    UI = 'save.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.dialog = loader.get('saved_message')
    
    def show(self, parent):
        self.dialog.set_transient_for(parent.window)
        self.dialog.run()

    def response_send(self, *args):
        self.dialog.hide()
