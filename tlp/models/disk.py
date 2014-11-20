class Disk:
    def __init__(self, id, alias='', size=''):
        self.id = id
        self.alias = alias
        self.size = size

    def know_as(self, name):
        return self.id == name or self.alias == name
