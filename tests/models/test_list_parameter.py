from unittest import TestCase
from tlpconfig.tlp.models import ListParameter


class TestListParameter(TestCase):
    def test_should_join_list_into_string_on_set_value(self):
        parameter = ListParameter('TEST')
        parameter.value = ['This', 'is', 'a', 'test.']

        self.assertEqual('"This is a test."', parameter._value)

    def test_should_split_value_by_spaces_on_get_value(self):
        parameter = ListParameter('TEST')
        parameter._value = '"This is a test."'

        self.assertEqual(['This', 'is', 'a', 'test.'], parameter.value)
