from tlp.models import NumericParameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestNumericParameter(TestCase):
    def test_should_cast_value_to_string_on_set_value(self):
        parameter = NumericParameter('TEST')
        parameter.value = 256.5

        self.assertEqual('256.5', parameter._value)

    def test_should_cast_value_to_int_on_get_value(self):
        parameter = NumericParameter('TEST')
        parameter._value = '512.5'

        self.assertEqual(512.5, parameter.value)

    def test_should_remove_decimal_places_for_integer_numbers(self):
        parameter = NumericParameter('TEST')
        parameter.value = float(245.0)

        self.assertEqual('245', parameter._value)

    def test_parameter_should_clone_itself(self):
        param = NumericParameter('Test', reboot_needed=True)
        param.initialize(True, 111)
        clone = param.clone()

        self.assertEqual(param.reboot_needed, clone.reboot_needed)
        self.assertEqual(param._active, clone._active)
        self.assertEqual(param._value, clone._value)
        self.assertEqual(param.name, clone.name)

    def test_should_notify_when_set_value(self):
        param = NumericParameter('TEST')
        param.initialize(True, '123')
        param.notify_changes = MagicMock()
        param.value = 321
        self.assertTrue(param.notify_changes.called)

    def test_parameter_should_not_notify_when_set_value_with_same_value(self):
        param = NumericParameter('TEST')
        param.initialize(True, '123')
        param.notify_changes = MagicMock()
        param.value = 123
        self.assertFalse(param.notify_changes.called)
