from .. import ChangesNotifier
from . import Group


class CompositeGroup(ChangesNotifier):
    def __init__(self, head, subgroups):
        ChangesNotifier.__init__(self)
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
        self.header.active = value
        self.notify_changes()

    def expand(self):
        for param in self.parameters:
            param.expand([disk.id for disk in self.head.disks])

    def _head_changed(self, head):
        enabled = [uid for uid in head.order if head.parameters[uid].value]
    
        for param in self.tail:
            param.order = enabled

    def subgroups(self):
        return {disk.id: self._create_subgroups(disk.id, self._subgroups)
                for disk in self.head.disks}

    def _create_subgroups(self, uid, groups):
        return [Group(name, [param.parameters[uid] for param in parameters])
                for name, parameters in groups.items()]
