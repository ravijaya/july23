"""to delete an item from a dict object"""

info = {
    'host': ['ws1', 'ws2'],
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,  # to be updated....

}


value = info.pop('desc')  # delete the element for the key, returns its value
print(value)
print()
info.pop('host')
print(info)