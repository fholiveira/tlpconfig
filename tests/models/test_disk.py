from unittest import TestCase
from tlp.models import Disk


class TestDisk(TestCase):
    def test_disk_should_be_known_by_id(self):
        disk = Disk('disk1', alias='sda', size='256GB')
        self.assertTrue(disk.know_as('disk1'))

    def test_disk_should_be_known_by_alias(self):
        disk = Disk('disk1', alias='sda', size='256GB')
        self.assertTrue(disk.know_as('sda'))
