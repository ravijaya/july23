"""demo for the bytes string"""
"""http://collabedit.com/fwra4"""
import subprocess
import sys
import re

pattern = r'\b([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.'
pattern += '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){2}'
pattern += r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\b'

print(pattern)
print()
if sys.platform in ['linux', 'darwin']:
    cmd = ['ifconfig']
else:
    cmd = ['ipconfig']

op = subprocess.check_output(cmd).decode()  #
op = '10012.12.12.12' + op

for m in re.finditer(pattern, op):
    print(m.group())

