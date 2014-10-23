from gi.repository import Gtk


class Builder():
    def __init__(self):
        self.builder = Gtk.Builder()

    def load(self, file):
        self.builder.add_from_file(file)

    def connect(self, handler):
        return self.builder.connect_signals(handler)

    def get(self, object_name):
        return self.builder.get_object(object_name)
