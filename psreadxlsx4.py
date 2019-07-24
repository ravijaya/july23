import pyexcel as p
import pprint


def by_uid(row):
    return int(row[2])


rows = [row for row in p.get_sheet(file_name='passwd.xlsx')]
# rows.sort(key=by_uid)
rows = sorted(rows, key=by_uid, reverse=True)
pprint.pprint(rows)

p.save_as(dest_file_name='reversedbyuid.xlsx', array=rows)
