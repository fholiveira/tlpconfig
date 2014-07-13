from tlp.views.categories import *
from tlp.views import Status, create_category_loader 
from gi.repository import Gtk


class Window():
    UI = ('window.ui', 'header.ui')

    def __init__(self, loader):
        loader.connect(self)

        self._load_childs(loader)

    def load_configuration(self, configuration):
        self.config = configuration

        load_view = create_category_loader(configuration.parameters)
        self.categories = [load_view(FileSystem), 
                           load_view(ProcessorAndFrequenceScaling),
                           load_view(Kernel),
                           load_view(Undervolting),
                           load_view(DisksAndControllers),
                           load_view(PciExpressBus),
                           load_view(GraphicsCards),
                           load_view(Networking),
                           load_view(Audio),
                           load_view(DriveSlotUltrabay),
                           load_view(RuntimePowerManagement),
                           load_view(Usb),
                           load_view(SystemStartAndShutdown),
                           load_view(WirelessRadioSwitch),
                           load_view(BatteryChargeThresholds)]

        self._list_categories()

    def save(self, button):
        print('Save!')

    def save_as(self, button):
        buttons = (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                   Gtk.STOCK_SAVE, Gtk.ResponseType.OK)

        dialog = Gtk.FileChooserDialog('Save TLP configuration file',
                                       self.window, Gtk.FileChooserAction.SAVE,
                                       buttons)

        if dialog.run() == Gtk.ResponseType.OK:
            print("File selected: " + dialog.get_filename())
    
        dialog.destroy()

    def status(self, button):
        load_view(Status).show(self.window)

    def show(self):
        self.window.present()

    def select_row(self, listbox, row):
        if row:
            self.stack.set_visible_child_name(Gtk.Buildable.get_name(row))

    def _load_childs(self, loader):
        self.panel = loader.get('panel')
        self.window = loader.get('window')
        self.categories_list = loader.get('categories')

        self.stack = Gtk.Stack()
        self.stack.set_visible(True)
        loader.get('category_content').add(self.stack)

        self.window.set_titlebar(loader.get('header'))

    def _list_categories(self):
        def header(row, before, user_data):
            if before and not row.get_header():
                sep = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
                row.set_header(sep)

        self.categories_list.set_header_func(header, None)

        for category in self.categories:
            self.categories_list.add(category.menu)
            self.stack.add_named(category.panel,
                                 Gtk.Buildable.get_name(category.menu))
