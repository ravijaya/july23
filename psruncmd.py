"""demo for the bytes string"""

import subprocess
import sys

if sys.platform in ['linux', 'darwin']:
    cmd = ['ifconfig']
else:
    cmd = ['ipconfig']

op = subprocess.check_output(cmd).decode()  #
print(op)