"""
syntax for the slicing
~~~~~~~~~~~~~~~~~~~~~~

    name[start-index:ex-of-end-index]

"""

s = 'perlandpython'

print(s[:4])
print(s[3:7])
print(s[-6:])
print(s[:])
print(s[1:-1])
print(s[-6:-3])

s = 'inet 192.168.3.158  netmask 255.255.255.0  broadcast 192.168.3.255'

if '192.168.3.158' in s:
    print(s.split())
    print(s.split()[:3])