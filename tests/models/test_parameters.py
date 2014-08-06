from unittest import TestCase
from tlp.models.parameter import Parameter


class TestParameter(TestCase):

    def test_should_be_changed_if_value_has_changed(self):
        parameter = Parameter('TEST')
        parameter.initial_state = {'active': True, 'value': '1'}
        parameter.active = True
        parameter._value = '2'

        self.assertTrue(parameter.is_changed())

    def test_should_be_changed_if_active_state_has_changedi_to_true(self):
        parameter = Parameter('TEST')
        parameter.initial_state = {'active': False, 'value': '1'}
        parameter.active = True
        parameter._value = '1'

        self.assertTrue(parameter.is_changed())

    def test_should_be_changed_if_active_state_has_changedi_to_false(self):
        parameter = Parameter('TEST')
        parameter.initial_state = {'active': True, 'value': '1'}
        parameter.active = False
        parameter._value = '1'

        self.assertTrue(parameter.is_changed())

    def test_should_not_be_changed_if_parameter_has_always_not_active(self):
        parameter = Parameter('TEST')
        parameter.initial_state = {'active': False, 'value': '1'}
        parameter.active = False
        parameter._value = '2'

        self.assertFalse(parameter.is_changed())

    def test_should_write_commented_parameter(self):
        parameter = Parameter('TEST')
        parameter.initial_state = {'active': True, 'value': '1'}
        parameter.active = False
        parameter._value = '2'

        self.assertEqual('#TEST=2', parameter.write('TEST=1'))

    def test_should_write_not_commented_parameter(self):
        parameter = Parameter('TEST')
        parameter.initial_state = {'active': False, 'value': '1'}
        parameter.active = True
        parameter._value = '254'

        self.assertEqual('TEST=254', parameter.write('#TEST=1'))
