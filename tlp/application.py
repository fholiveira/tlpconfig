from gi.repository import Gtk, Gio, Gdk
from tlp.views import Window

class App(Gtk.Application):
    
    def __init__(self):
        Gtk.Application.__init__(self,application_id='TLP.Configuration')
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = Window(self)
            self.add_window(self.window.window)
            self.window.show()

        self.window.present()
        
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('tlp/ui/shell.css')

        context = Gtk.StyleContext()
        context.add_provider_for_screen(Gdk.Screen.get_default(),
                                        css_provider,
                                        Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def do_startup(self):
        Gtk.Application.do_startup(self)
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file('tlp/ui/shell.ui')
        
        appmenu = self.builder.get_object('appmenu')
        self.set_app_menu(appmenu)

        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.about_cb)
        self.add_action(about_action)

        quit_action = Gio.SimpleAction.new('quit', None)
        quit_action.connect('activate', self.quit_cb)
        self.add_action(quit_action)

    def about_cb(self, action, parameter):
        aboutdialog = Gtk.AboutDialog()
        aboutdialog.set_title('About TLP Configuration')
        aboutdialog.set_program_name('TLP Configuration')

        _shell = GnomeShellFactory().get_shell()
        if _shell is not None:
            aboutdialog.set_comments('GNOME Shell {0} ({1} mode)'.format(_shell.version, _shell.mode))
        else:
            aboutdialog.set_comments('GNOME Shell not running')

        aboutdialog.set_copyright('Copyright \xc2\xa9 2011 - 2013 John Stowers.')
        aboutdialog.set_logo_icon_name('tlp-configuration')
        aboutdialog.set_website('https://github.com/fholiveira') 
        aboutdialog.set_website_label(_('Homepage'))
        aboutdialog.set_license_type(Gtk.License.GPL_3_0)
        aboutdialog.set_authors(['Fernando Oliveira <fernando@fholiveira.com>'])             
        aboutdialog.connect('response', lambda w, r: aboutdialog.destroy())
        aboutdialog.show()

    def quit_cb(self, action, parameter):
        self.quit()
