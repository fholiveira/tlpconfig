from .. import ChangesNotifier
from . import Group


class CompositeGroup(ChangesNotifier):
    def __init__(self, ordered_options, head, subgroups):
        ChangesNotifier.__init__(self)
        self.options = ordered_options
        self._subgroups = subgroups

        self.head = head
        self.head.watch(self._head_changed)

        self.tail = [param for group in subgroups.values() for param in group]
        self.parameters = [self.head] + self.tail

        self.expand()

    @property
    def is_active(self):
        return self.head.active
    
    @is_active.setter
    def is_active(self, value):
        fself.header.active = value
        self.notify_changes()

    def expand(self):
        for param in self.parameters:
            param.expand(self.options)
        
        for uid in self.options:
            self.head.parameters[uid].yes = uid
            self.head.parameters[uid].no = ''
            self.head.parameters[uid].notify_changes()

    def _head_changed(self, head):
        enabled = [uid for uid in self.options if head.parameters[uid].value]
    
        for param in self.tail:
            param.order = enabled

    def subgroups(self):
        return {uid: self._create_subgroups(uid, self._subgroups)
                for uid in self.options }

    def _create_subgroups(self, uid, groups):
        return [Group(name, [param.parameters[uid] for param in parameters])
                for name, parameters in groups.items()]
