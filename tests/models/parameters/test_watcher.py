from tlp.models import (BooleanParameter, NumericParameter, ListParameter,
                        ParameterWatcher)
from unittest.mock import MagicMock
from unittest import TestCase


class TestParameterWatcher(TestCase):
    def setUp(self):
        self.watcher = ParameterWatcher([BooleanParameter('boolean'),
                                         NumericParameter('numeric'),
                                         ListParameter('list',
                                                       reboot_needed=True)])
        self.watcher.parameters[0].value = True
        self.watcher.parameters[1].value = 123
        self.watcher.parameters[2].value = 'abc'
        self.watcher.remember_state()
    
    def test_needs_reboots_when_a_need_reboot_paramester_has_been_changed(self):
        self.watcher.parameters[2].value = 'xyz'
        self.assertTrue(self.watcher.need_reboot_to_apply())

    def test_should_detect_changes(self):
        self.watcher.parameters[0].value = False
        self.assertTrue(self.watcher.has_changes())

    def test_should_detect_what_parameters_has_changes(self):
        param = self.watcher.parameters[1]
        param.value = 987
        self.assertListEqual([param], self.watcher.changed_parameters())

    def test_remember_state(self):
        self.watcher.parameters[1].value = 987
        self.watcher.parameters[2].value = 'xyz'

        self.watcher.remember_state()

        self.assertFalse(self.watcher.has_changes())

    def test_should_notify_when_state_changed(self):
        self.watcher.notify_changes = MagicMock()
        self.watcher.parameters[2].value = 'xyz'
        self.assertTrue(self.watcher.notify_changes.called)
