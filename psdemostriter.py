"""iterator"""

s = 'this is a sample string in python'

for temp in s:
    if temp not in 'aeiou ':  # membership test operator
        print(temp, ':', ord(temp))
    else:
        print('**')
