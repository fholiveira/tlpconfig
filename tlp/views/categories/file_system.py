from gi.repository import Gtk


class FileSystem():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('tlp/ui/categories/file_system.ui')
        builder.connect_signals(self)
        
        self.menu = builder.get_object('file_system_row')
        self.panel = builder.get_object('file_system_panel')
