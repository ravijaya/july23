"""demo for the regex pattern matching"""

import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match

m = re.search(pattern, s, re.I)

if m:
    """match block"""
    print('match string :', m.group())
    start, end = m.span()
    before = s[:start]   # slicing
    print('before :', before)
    after = s[end:]
    print(after)
else:
    print('failed to match')
