"""demo for the matching multiple times"""

import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # non-greedy match


for m in re.finditer(pattern, s, re.I):
    a = m
    # print(a)
    print(a.group())
    print(m.span())
    print()