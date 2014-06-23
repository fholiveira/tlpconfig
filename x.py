from gi.repository import Gtk

class Handler:
    def on_delete(self, *args):
        Gtk.main_quit(*args)

builder = Gtk.Builder()
builder.add_from_file("window.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

categories = builder.get_object("categories")
print (categories)
Gtk.main()
