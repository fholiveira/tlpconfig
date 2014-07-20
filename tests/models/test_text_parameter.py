from unittest import TestCase
from tlp.models.parameter import TextParameter


class TestTextParameter(TestCase):
    def test_should_set_delimiter_on_set_value(self):
        parameter = TextParameter('TEST', quotes='#')
        parameter.value = 'test'

        self.assertEqual('#test#', parameter._value)

    def test_should_remove_delimiter_on_get_value(self):
        parameter = TextParameter('TEST', quotes='#')
        parameter._value = '#test#'

        self.assertEqual('test', parameter.value)
