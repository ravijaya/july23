"""demo for the lookup aka read operation"""

info = {
    'host': ['ws1', 'ws2'],
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,  # to be updated....

}


print(info.keys())  # keys for each item
print()
print(info.values())
print()
print(info.items())