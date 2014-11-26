from tlp.models import ChangesNotifier
from unittest.mock import MagicMock
from unittest import TestCase


class TestChangesNotifier(TestCase):
    def test_should_register_handler(self):
        changes = ChangesNotifier()
        handler1 = lambda p: None
        handler2 = lambda p: None

        changes.watch(handler1)
        changes.watch(handler2)

        self.assertListEqual([handler1, handler2],
                             changes.changes_handlers)

    def test_should_call_handler_on_notify(self):
        changes = ChangesNotifier()
        handler1 = lambda p: None
        handler2 = MagicMock()
        changes.watch(handler1)
        changes.watch(handler2)
   
        changes.notify_changes()

        handler2.assert_called_with(changes)     
