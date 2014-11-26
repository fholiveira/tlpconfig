import tlp.models.commands as commands
from unittest import TestCase
from tlp.models import Disk


class TestCommands(TestCase):
    def setUp(self):
        def run(arg):
            if arg == 'tlp diskid':
                return "sda: disk1\nsdb: disk2" 
            return "sda 256G\nsdb 128G"

        commands._run_command = run 

    def test_get_tlpstatus(self):
        commands._run_command = lambda s: 'status'
        self.assertEqual('status', commands.get_status())

    def test_get_disks_should_return_2_disks(self):
        disks = commands.get_disks()
        self.assertEqual(len(disks), 2)
        
    def test_get_disks_should_get_disks_ids(self):
        disks = commands.get_disks()
        self.assertListEqual(['disk1', 'disk2'],
                             [disk.id for disk in disks]) 
        
    def test_get_disks_should_get_disks_aliases(self):
        disks = commands.get_disks()
        self.assertListEqual(['sda', 'sdb'],
                             [disk.alias for disk in disks]) 
        
    def test_get_disks_should_get_disks_sizes(self):
        disks = commands.get_disks()
        self.assertListEqual(['256G', '128G'],
                             [disk.size for disk in disks]) 
