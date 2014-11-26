from tlp.models import ListParameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestListParameter(TestCase):
    def test_should_join_list_into_string_on_set_value(self):
        parameter = ListParameter('TEST')
        parameter.value = ['This', 'is', 'a', 'test.']

        self.assertEqual('"This is a test."', parameter._value)

    def test_should_split_value_by_spaces_on_get_value(self):
        parameter = ListParameter('TEST')
        parameter._value = '"This is a test."'

        self.assertEqual(['This', 'is', 'a', 'test.'], parameter.value)

    def test_parameter_should_clone_itself(self):
        param = ListParameter('Test', reboot_needed=True)
        param.initialize(True, 'v1 v2 v3')
        clone = param.clone()

        self.assertEqual(param.reboot_needed, clone.reboot_needed)
        self.assertEqual(param._active, clone._active)
        self.assertEqual(param._value, clone._value)
        self.assertEqual(param.name, clone.name)

    def test_should_notify_when_set_value(self):
        param = ListParameter('TEST')
        param.initialize(True, '"a b c"')
        param.notify_changes = MagicMock()
        param.value = ['a', 'b', 'd']
        self.assertTrue(param.notify_changes.called)

    def test_parameter_should_not_notify_when_set_value_with_same_value(self):
        param = ListParameter('TEST')
        param.initialize(True, '"a b c"')
        param.notify_changes = MagicMock()
        param.value = ['a', 'b', 'c']
        self.assertFalse(param.notify_changes.called)
