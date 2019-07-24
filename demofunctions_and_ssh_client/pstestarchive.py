from psmakearchive import make_archive
from glob import glob
from time import ctime

list_of_files = glob('*.py')
print(list_of_files)
print()
make_archive('src{}.zip'.format(ctime()), *list_of_files)  # passing content of the list as argument