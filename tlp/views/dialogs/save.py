from gi.repository import Gtk


class SaveDialogView:
    def __init__(self):
       self.dialog = self._create()
       self.filename = ''

    def _create(self):
        buttons = (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                   Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        dialog = Gtk.FileChooserDialog('Save TLP configuration file',
                                       None, Gtk.FileChooserAction.SAVE,
                                       buttons)
        dialog.set_default_size(500, 600)
        return dialog

    def show(self, parent):
        self.dialog.set_transient_for(parent.window)

        success = self.dialog.run() == Gtk.ResponseType.OK
        self.filename = self.dialog.get_filename() if success else ''

        self.dialog.destroy()
        return success 
