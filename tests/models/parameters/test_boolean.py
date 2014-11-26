from tlp.models import BooleanParameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestBooleanParameter(TestCase):
    def test_should_set_custom_flag_on_set_value(self):
        parameter = BooleanParameter('TEST', yes='@@@', no='***')
        parameter.value = True

        self.assertEqual('@@@', parameter._value)

    def test_should_use_custom_flag_on_get_value(self):
        parameter = BooleanParameter('TEST', yes='@@@', no='***')
        parameter._value = '***'

        self.assertFalse(parameter.value)

    def test_should_use_default_flag_on_set_value(self):
        parameter = BooleanParameter('TEST')
        parameter.value = True

        self.assertEqual('1', parameter._value)

    def test_should_use_default_flag_on_get_value(self):
        parameter = BooleanParameter('TEST')
        parameter._value = '0'

        self.assertFalse(parameter.value)

    def test_parameter_should_clone_itself(self):
        param = BooleanParameter('Test', yes=111, no=222, reboot_needed=True)
        param.initialize(True, 111)
        clone = param.clone()

        self.assertEqual(param.reboot_needed, clone.reboot_needed)
        self.assertEqual(param._active, clone._active)
        self.assertEqual(param._value, clone._value)
        self.assertEqual(param.name, clone.name)
        self.assertEqual(param.yes, clone.yes)
        self.assertEqual(param.no, clone.no)

    def test_should_notify_when_set_value(self):
        param = BooleanParameter('TEST')
        param.initialize(True, '1')
        param.notify_changes = MagicMock()
        param.value = False
        self.assertTrue(param.notify_changes.called)

    def test_parameter_should_not_notify_when_set_value_with_same_value(self):
        param = BooleanParameter('TEST')
        param.initialize(True, '1')
        param.notify_changes = MagicMock()
        param.value = True
        self.assertFalse(param.notify_changes.called)
