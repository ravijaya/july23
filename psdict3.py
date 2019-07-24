"""dict update, add, validate for the key operation"""

info = {
    '1001': {
        'name': 'sam',
        'marks': [2, 3, 4, 5, 6]
    },
    '1002': {
        'name': 'pam',
        'marks': [12, 3, 14, 15, 16]
    },
}

item = 'version'

if item in info:   # validate for the key, checking for the key in dict
    info[item] = 3.6 # update

print(info)
print()
info['arch'] = 'x86_64'  # add an element to the dict
print(info)
print()

