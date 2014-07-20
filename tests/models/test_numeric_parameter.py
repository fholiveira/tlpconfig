from unittest import TestCase
from tlp.models.parameter import NumericParameter


class TestNumericParameter(TestCase):
    def test_should_cast_value_to_string_on_set_value(self):
        parameter = NumericParameter('TEST')
        parameter.value = 256

        self.assertEqual('256', parameter._value)

    def test_should_cast_value_to_int_on_get_value(self):
        parameter = NumericParameter('TEST')
        parameter._value = '512'

        self.assertEqual(512, parameter.value)
