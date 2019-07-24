"""demo for the lookup aka read operation"""

info = {
    'host': ['ws1', 'ws2'],
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,  # to be updated....

}


print(info['host'])   # read
print(info['domain'])
print(info['app'])