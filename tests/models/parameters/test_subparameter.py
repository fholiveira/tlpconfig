from tlp.models import Subparameter, BooleanParameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestSubParameter(TestCase):
    def setUp(self):
        self.param = Subparameter(BooleanParameter('TEST'))
        self.param.expand(['disk1', 'disk2'])

    def test_should_set_value_on_initialize(self):
        self.param.initialize(False, '1 1')
        self.assertEqual('1 1', self.param.value)

    def test_should_set_active_on_initialize(self):
        self.param.initialize(False, '1 1')
        self.assertFalse(self.param.active)

    def test_shoul_expand_parameter(self):
        self.assertEqual(len(self.param.parameters), 2)

    def test_should_set_order_when_expand(self):
        self.param.expand(['disk2', 'disk1'])
        self.assertEqual(['disk2', 'disk1'], self.param.order)

    def test_update_activity_of_subparameter_when_set_allowed_value(self):
        self.param.initialize(True, '1 0')
        self.param.value = '0 0'
        self.assertTrue(all(param.active
                             for param in self.param.parameters.values()))

    def test_update_activity_of_subparameter_when_set_disallowed_value(self):
        self.param.initialize(True, '1 0')
        self.param.value = 'keep _'
        self.assertFalse(any(param.active
                             for param in self.param.parameters.values()))

    def test_should_not_set_skip_caracters_on_value(self):
        self.param.initialize(True, '1 0')
        self.param.value = 'keep _'
        self.assertFalse(any(param 
                             for param in self.param.parameters.values()
                             if param._value in ('keep', '_')))

    def test_should_notify_when_set_value(self):
        self.param.initialize(True, '1 0')
        self.param.notify_changes = MagicMock()
        self.param.value = '1 1'
        self.assertTrue(self.param.notify_changes.called)

    def test_should_not_notify_when_set_value_to_same_value(self):
        self.param.initialize(True, '1 0')
        self.param.notify_changes = MagicMock()
        self.param.value = '1 0'
        self.assertFalse(self.param.notify_changes.called)

    def test_should_notify_when_set_subparameter_value(self):
        self.param.initialize(True, '1 0')
        self.param.notify_changes = MagicMock()
        self.param.parameters['disk2'].value = True
        self.assertTrue(self.param.notify_changes.called)
