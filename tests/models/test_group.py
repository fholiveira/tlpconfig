from unittest import TestCase
from tlp.models import Group, TextParameter


class TestGroup(TestCase):
    def setUp(self):
        self.group = Group('TEST', {'PARAM1': TextParameter('PARAM1'), 
                                    'PARAM2': TextParameter('PARAM2'),
                                    'PARAM3': TextParameter('PARAM3')})

    def test_should_be_active_when_all_params_are_active(self):
        self.group.parameters['PARAM1'].active = True
        self.group.parameters['PARAM2'].active = True
        self.group.parameters['PARAM3'].active = True

        self.assertTrue(self.group.is_active)

    def test_should_not_be_active_when_one_param_is_not_active(self):
        self.group.parameters['PARAM1'].active = True
        self.group.parameters['PARAM2'].active = False
        self.group.parameters['PARAM3'].active = True

        self.assertFalse(self.group.is_active)

    def test_should_set_active_state_on_child_parameters(self):
        self.group.parameters['PARAM1'].active = False
        self.group.parameters['PARAM2'].active = True
        self.group.parameters['PARAM3'].active = False

        self.group.is_active = True

        self.assertTrue(all(param.active 
                            for param 
                            in self.group.parameters.values()))
