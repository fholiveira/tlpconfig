from tlp.views.binders import ParameterBinderSelector, GroupBinder
from gi.repository import Gtk
from datetime import timedelta

class DiskOptionsView:
    UI = 'categories/disk.ui'

    def __init__(self, loader):
        self.controls = loader.get('options')
        self.loader = loader

        self.header = Gtk.Label()
        self.header.set_hexpand(True)

        self.scale = [(  1, lambda x: 'Disabled'),
                      (241, lambda x: str(timedelta(seconds=x * 5))),
                      (252, lambda x: str(timedelta(minutes=(x -240) * 30)))]

        loader.get('DISK_SPINDOWN_TIMEOUT_ON_AC').connect('format-value',
                                                          self._scale_changed)
        loader.get('DISK_SPINDOWN_TIMEOUT_ON_BAT').connect('format-value',
                                                           self._scale_changed)
        loader.get('DISK_DEVICES').connect('notify::active',
                                           self._active_options)

    def _active_options(self, switch, arg):
        self.loader.get('DISK_CONFIG').set_sensitive(switch.get_active())

    def _scale_changed(self, scale, value):
        return next(func(value) for index, func in self.scale
                    if value < index)

    def set_header(self, text):
        self.header.set_text(text)

    def bind_groups(self, head, groups):
        selector = ParameterBinderSelector()

        head_binder = selector.get_from(head)
        head_binder.bind(self.loader.get(head.name))

        group_binders = [GroupBinder(selector, group) for group in groups]
        for binder in group_binders:
            binder.bind(self.loader)

        self.binders = [head_binder] + group_binders
