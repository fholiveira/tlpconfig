class Category:
    def __init__(self, category, loader):
        loader.connect(self)
        self.loader = loader

        self.menu = loader.get('_'.join([category.lower(), 'row']))
        self.panel = loader.get('_'.join([category.lower(), 'panel']))

    def load_control(self, control_id):
        return self.loader.get(control_id);
