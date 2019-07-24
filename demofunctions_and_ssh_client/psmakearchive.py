"""archives in python"""
from zipfile import ZipFile


def make_archive(archive_name, *args):
    """example variable len argument parameter"""

    with ZipFile(archive_name, mode='w') as zf:
        for file_name in args:
            zf.write(file_name)
            print(file_name, ': added')

