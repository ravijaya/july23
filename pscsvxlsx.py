import csv
import pyexcel


def csv2xlsx(csv_file, spreadsheet_file):
    #data = []

    #for row in csv.reader(open(csv_file), delimiter=':'):
    #    data.append(row)

    # list comprehension
    data = [row for row in csv.reader(open(csv_file), delimiter=':')]
    pyexcel.save_as(dest_file_name=spreadsheet_file, array=data)


csv2xlsx('passwd.txt', 'passwd.xlsx')
