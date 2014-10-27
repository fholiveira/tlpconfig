from .views import MainView, ViewFactory, load_css 
from gi.repository import Gtk, Gio, Gdk
from .controllers import MainController
from .models import Configuration


class App(Gtk.Application):
    
    def __init__(self):
        Gtk.Application.__init__(self, application_id='TLP.Configuration')
        self.window = None

    def start(self, config_file):
        self.config = Configuration(config_file)
        self.run(None)

    def do_activate(self):
        load_css('application.css', Gdk.Screen.get_default())
        self.window.show()
        
    def do_startup(self):
        Gtk.Application.do_startup(self)
       
        factory = ViewFactory()
        if not self.window:
            self.window = factory.create(MainController(self.config))
            self.add_window(self.window.window)
 
        self.set_app_menu(self.window.appmenu)
        self._bind_actions()

    def _bind_actions(self):
        about_action = Gio.SimpleAction.new('show_about', None)
        about_action.connect('activate', self.window.show_about)
        self.add_action(about_action)

        preferences_action = Gio.SimpleAction.new('show_preferences', None)
        preferences_action.connect('activate', self.window.show_preferences)
        self.add_action(preferences_action)

        quit_action = Gio.SimpleAction.new('quit', None)
        quit_action.connect('activate', lambda *args: self.quit())
        self.add_action(quit_action)
