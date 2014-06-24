from gi.repository import Gtk, Gio, Gdk
from tlp.views import Window, ViewLoader

class App(Gtk.Application):
    
    def __init__(self):
        Gtk.Application.__init__(self, application_id='TLP.Configuration')
        self.window = None

    def do_activate(self):
        ViewLoader.load_css('tlp/ui/shell.css', Gdk.Screen.get_default())

        if not self.window:
            self.window = Window(self)
            self.add_window(self.window.window)
            self.window.show()

        self.window.present()
        
    def do_startup(self):
        Gtk.Application.do_startup(self)
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file('tlp/ui/shell.ui')
        
        appmenu = self.builder.get_object('appmenu')
        self.set_app_menu(appmenu)

        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.about)
        self.add_action(about_action)

        quit_action = Gio.SimpleAction.new('quit', None)
        quit_action.connect('activate', lambda *args: self.quit())
        self.add_action(quit_action)

    def about(self, action, parameter):
        ViewLoader('tlp/ui/about.ui').get('about').show()
