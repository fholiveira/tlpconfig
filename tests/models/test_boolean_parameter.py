from unittest import TestCase
from tlp.models.parameter import BooleanParameter


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
