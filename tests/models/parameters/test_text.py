from tlp.models import TextParameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestTextParameter(TestCase):
    def test_should_set_delimiter_on_set_value(self):
        parameter = TextParameter('TEST', quotes='#')
        parameter.value = 'test'

        self.assertEqual('#test#', parameter._value)

    def test_should_remove_delimiter_on_get_value(self):
        parameter = TextParameter('TEST', quotes='#')
        parameter._value = '#test#'

        self.assertEqual('test', parameter.value)

    def test_parameter_should_clone_itself(self):
        param = TextParameter('Test', quotes="$", reboot_needed=True)
        param.initialize(True, '$aaaaaaaa$')
        clone = param.clone()

        self.assertEqual(param.reboot_needed, clone.reboot_needed)
        self.assertEqual(param._active, clone._active)
        self.assertEqual(param._value, clone._value)
        self.assertEqual(param.quotes, clone.quotes)
        self.assertEqual(param.name, clone.name)

    def test_should_notify_when_set_value(self):
        param = TextParameter('TEST')
        param.initialize(True, 'abc')
        param.notify_changes = MagicMock()
        param.value = 'xyz'
        self.assertTrue(param.notify_changes.called)

    def test_parameter_should_not_notify_when_set_value_with_same_value(self):
        param = TextParameter('TEST')
        param.initialize(True, 'abc')
        param.notify_changes = MagicMock()
        param.value = 'abc'
        self.assertFalse(param.notify_changes.called)
