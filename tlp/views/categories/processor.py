from gi.repository import Gtk


class ProcessorAndFrequenceScaling():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file('tlp/ui/categories/processor.ui')
        builder.connect_signals(self)
        
        self.menu = builder.get_object('processor_row')
        self.panel = builder.get_object('processor_panel')
