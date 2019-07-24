"""dict update, add, validate for the key operation"""

info = {
    'host': ['ws1', 'ws2'],
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,  # to be updated....

}

item = 'version'

if item in info:   # validate for the key, checking for the key in dict
    info[item] = 3.6 # update

print(info)
print()
info['arch'] = 'x86_64'  # add an element to the dict
print(info)
print()

