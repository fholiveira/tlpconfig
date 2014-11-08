from subprocess import Popen, PIPE


def _run_command(command_text):
    process = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()

    if error:
        return error.decode('UTF-8')

    return output.decode('UTF-8')

    
def get_status():
    _run_command('tlp-stat')


def get_disks():
    disknames = _run_command('lsblk --nodeps -n --output NAME,SIZE').split('\n')
    disknames = (name.split() for name in disknames if name)
    disknames = {name: '{0} - {1}'.format(name, diskid) 
                 for name, diskid in disknames}
  
    diskids = _run_command('tlp diskid').split('\n')
    diskids = (diskid.split(': ') for diskid in diskids if diskid)
    return [(diskid, disknames[name]) for name, diskid in diskids]
