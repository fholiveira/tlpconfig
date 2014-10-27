from gi.repository import Gtk


class HomeStack:
    def __init__(self, welcome, editor):
        self.welcome = welcome
        self.editor = editor
        self.stack = self._create()

    def bind(self, panel, enable_on_editor):
        self.enable_on_editor = enable_on_editor
        panel.add(self.stack)

    def show_editor(self):
        self.stack.set_visible_child_name('editor')

    def show_welcome(self):
        self.stack.set_visible_child_name('welcome')

    def switch(self, is_enabled):
        if is_enabled:
            self.show_editor()
        else:
            self.show_welcome()

        for control in self.enable_on_editor:
            control.set_visible(is_enabled)

    def _create(self):
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        stack.set_homogeneous(False)
        stack.set_visible(True)
        
        stack.add_named(self.welcome, 'welcome')
        stack.add_named(self.editor, 'editor')

        return stack
