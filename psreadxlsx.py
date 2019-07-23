import pyexcel

# pyexcel.get_book
book = pyexcel.get_book(file_name='hosts.xlsx')

for sheet in book:
    print(sheet.name)
    for row in sheet:
        print(row)
    print()
