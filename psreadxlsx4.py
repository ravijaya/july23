import pyexcel as p
from pprint import pprint as pp  # cherry picking


def by_uid(row):
    return int(row[2])


rows = [row for row in p.get_sheet(file_name='passwd.xlsx')]
# rows.sort(key=by_uid)
rows = sorted(rows, key=by_uid, reverse=True)  # sorted the list based on a key
pp(rows)

p.save_as(dest_file_name='reversedbyuid.xlsx', array=rows)
