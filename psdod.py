"""dict of dicts...."""

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

print(info['1001']['marks'])
print(info['1001']['marks'][0])
print(info['1001']['marks'][1])
print(sum(info['1001']['marks']))
print(sum(info['1001']['marks'])/len(info['1001']['marks']))
print(info['1001']['name'])
