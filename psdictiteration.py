"""demo for the dict iteration"""

info = {
    'host': ['ws1', 'ws2'],
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,  # to be updated....
}

for key, value in info.items():
    if type(value) is list:    # type validation
        print(key, ':')
        for item in value:   # iterate for the list
            print("\t", item)
        continue   # control to the next iteration

    print(key, '->', value)
