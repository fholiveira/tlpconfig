from subprocess import Popen, PIPE
from collections import namedtuple
from . import Disk


def _run_command(command_text):
    process = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()

    if error:
        return error.decode('UTF-8')

    return output.decode('UTF-8')

    
def get_status():
    return _run_command('tlp-stat')


def get_disks():
    lsblk = 'lsblk --nodeps -n --output NAME,SIZE'
    disksizes = _run_command(lsblk).split('\n')
    disksizes = (line.split() for line in disksizes if line)
    disksizes = {name: size for name, size in disksizes}

    diskids = _run_command('tlp diskid').split('\n')
    diskids = (diskid.split(': ') for diskid in diskids if diskid)

    return [Disk(diskid, alias=name, size=disksizes[name])
            for name, diskid in diskids]
