"""demo for the ssh client using python"""

import paramiko
from getpass import getpass

"""http://collabedit.com/fwra4"""

# below line aka parallel assignment

host, port, user, password = '192.168.0.14', 22, 'training', getpass()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # ack the key
ssh.connect(host, port, user, password)

jobs = ['ifconfig', 'date', 'free -m']
for job in jobs:
    stdin, stdout, stderr = ssh.exec_command(job)  # return std file desc
    output = stdout.read()  # read the entire op
    response = output if output else stderr.read()
    print("ssh response for the :", job, "\n", response.decode())  # bytes into unicode
    print()
ssh.close()
