"""demo for the bytes string"""
"""http://collabedit.com/fwra4"""

import subprocess
import sys
import re
from json import dump

pattern = r'\b([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-4])\.'
pattern += '((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){2}'
pattern += r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\b'

print(pattern)
print()
if sys.platform in ['linux', 'darwin']:
    cmd = ['ifconfig']
else:
    cmd = ['ipconfig']

op = subprocess.check_output(cmd).decode()  #
# op = '10012.12.12.12' + op
print("\n", op)

ip_addrs = []

for m in re.finditer(pattern, op):  # match multiple times
    ip_addrs.append(m.group())

nic_pattern = '([A-Za-z0-9]+): '   # grouping
list_of_nics = [m.group(1) for m in re.finditer(nic_pattern, op)] # list comp

print(list_of_nics)
print(ip_addrs)
print()

# create a dict from the list
print(zip(list_of_nics, ip_addrs))
# print(list(zip(list_of_nics, ip_addrs)))
address_info = dict(zip(list_of_nics, ip_addrs))

# serialize the obecject, dict 2 json
dump(address_info, open('ipv4.json', 'w'), indent=2)


