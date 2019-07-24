"""demo for the find & replacement"""

import re
from fileinput import input, filelineno  # stream reader

for line in input('passwd.txt', inplace=True, backup='.bak'):
    if filelineno() <= 10:
        line = re.sub(':', ',', line)

    print(line, end='')  # redirected to the file stream