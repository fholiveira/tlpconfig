from tlp.models import Disk, DiskParameter
from unittest.mock import MagicMock
from unittest import TestCase


class TestDiskParameter(TestCase):
    def setUp(self):
        self.param = DiskParameter('TEST',
                                   [Disk('disk1', alias='sda', size='24GB'),
                                    Disk('disk2', alias='sdb', size='8GB')])

        self.param.expand(['disk1', 'disk2'])

    def test_should_set_value_on_initialize(self):
        self.param.initialize(False, '"disk1 disk2"')
        self.assertEqual('"disk1 disk2"', self.param.value)

    def test_should_set_active_on_initialize(self):
        self.param.initialize(False, '""')
        self.assertFalse(self.param.active)

    def test_shoul_expand_parameter(self):
        self.assertEqual(len(self.param.parameters), 2)

    def test_should_set_all_subparameters_as_active_on_expand(self):
        self.assertTrue(all(subparam.active 
                            for subparam in self.param.parameters.values()))
    
    def test_should_set_true_part_of_subparmeters_on_expand(self):
        self.assertEqual('disk1', self.param.parameters['disk1'].yes)
        self.assertEqual('disk2', self.param.parameters['disk2'].yes)
    
    def test_should_set_false_part_of_subparmeters_on_expand(self):
        self.assertListEqual(['', ''],
                             [subparam.no
                              for subparam in self.param.parameters.values()])

    def test_should_ignore_values_with_are_not_disks_when_set_value(self):
        self.param.value = '"dvd disk2 test"'
        self.assertEqual('"disk2"', self.param.value)

    def test_should_update_order_when_set_value(self):
        self.param.value = '"disk2 disk1"'
        self.assertEqual(['disk2', 'disk1'], self.param.order)

    def teste_should_resolve_disk_aliases_when_set_value(self):
        self.param.value = '"sdb disk1"'
        self.assertEqual('"disk2 disk1"', self.param.value)

    def test_should_notify_when_set_value(self):
        self.param.initialize(True, '"disk1"')
        self.param.notify_changes = MagicMock()
        self.param.value = '"disk1 disk2"'
        self.assertTrue(self.param.notify_changes.called)

    def test_should_not_notify_when_set_value_to_same_value(self):
        self.param.initialize(True, '"disk1"')
        self.param.notify_changes = MagicMock()
        self.param.value = '"disk1"'
        self.assertFalse(self.param.notify_changes.called)

    def test_should_notify_when_set_subparameter_value(self):
        self.param.initialize(True, '"disk1"')
        self.param.notify_changes = MagicMock()
        self.param.parameters['disk2'].value = True
        self.assertTrue(self.param.notify_changes.called)
