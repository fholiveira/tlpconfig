from tlp.models.parameters import Parameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestParameter(TestCase):
    def test_should_remember_state(self):
        param = Parameter('TEST')
        param.initialize(False, 123)
        param.remember_state()
        param._value = 321
        self.assertEqual((False, 123), param.initial_state)

    def test_should_set_value_on_initialize(self):
        param = Parameter('TEST')
        param.initialize(False, 123)
        self.assertEqual(123, param._value)

    def test_should_set_active_on_initialize(self):
        param = Parameter('TEST')
        param.initialize(False, 123)
        self.assertFalse(param.active)

    def test_inactive_parameter_should_be_converted_to_text(self):
        param = Parameter('TEST')
        param.initialize(False, 123)
        self.assertEqual(("TEST=", "#TEST=123" ), param.to_text())

    def test_active_parameter_should_be_converted_to_text(self):
        param = Parameter('TEST')
        param.initialize(True, 123)
        self.assertEqual(("TEST=", "TEST=123" ), param.to_text())

    def test_should_create_a_tuple_with_represent_parameter(self):
        param = Parameter('TEST')
        param.initialize(False, 123)
        self.assertEqual((False, 123), param.to_tuple())

    def test_parameter_should_notify_when_set_active(self):
        param = Parameter('TEST')
        param.initialize(True, 123)
        param.notify_changes = MagicMock()
        param.active = False
        param.notify_changes.assert_any_call()

    def test_parameter_should_not_notify_when_set_active_with_same_value(self):
        param = Parameter('TEST')
        param.initialize(True, 123)
        param.notify_changes = MagicMock()
        param.active = True
        self.assertFalse(param.notify_changes.called)
