from tlp.models import get_status


class StatusView:
    UI = 'status.ui'

    def __init__(self, loader):
        loader.connect(self)
        self.dialog = loader.get('status')
        self.content = loader.get('content')

        self.content.set_text(get_status('tlp-stat'))

    def show(self, parent):
        self.dialog.set_transient_for(parent.window)
        self.dialog.run()
        self.dialog.hide()
