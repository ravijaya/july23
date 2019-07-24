"""demo for the regex find & replacement"""

import re

s = 'root:x:0:0:root:/root:/bin/bash'
pattern = ':'
replacement = ','

s2 = re.sub(pattern, replacement, s)
print(s2)
print()

s3 = re.sub('[AEIOU]', '*', s2, flags=re.I)
print(s3)
print()

s3 = re.sub('[AEIOU]', '*', s2, flags=re.I, count=3)  # replace for n matches
print(s3)
print()
