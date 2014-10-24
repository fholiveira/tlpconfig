class ChangesNotifier:
    def __init__(self):
        self.changes_handlers = []

    def watch(self, handler):
        self.changes_handlers.append(handler)

    def notify_changes(self):
        for handler in self.changes_handlers:
            handler(self)
