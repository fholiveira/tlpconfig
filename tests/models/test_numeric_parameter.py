from unittest import TestCase
from tlpconfig.tlp.models import NumericParameter


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
