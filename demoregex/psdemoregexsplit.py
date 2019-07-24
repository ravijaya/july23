"""demo for the regex split"""
import re

pattern = ' +|[:,;]'

for line in open('listing.dat'):
    print(re.split(pattern, line)[4])