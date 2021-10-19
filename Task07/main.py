import csv

import Task07.main

csv.register_dialect('my_dialect', delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
# print(csv.list_dialects())


# with open('task07.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['qqq1', 'qqq2', '2222'])
#
# with open('task07.csv', 'r', newline='') as csv_file:
#     reader = csv.reader(csv_file, 'my_dialect')
#     for row in reader:
#         print(row[0])


# dictWriter
with open('task07.csv', 'w', newline='') as csv_file:
    header = ['col1_name', 'col2_name', 'col3_name']
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    writer.writerow({'col1_name': 'qqq1', 'col2_name': 'qqq2', 'col3_name': '2222'})
    writer.writerow({'col1_name': 'aaa1', 'col2_name': 'aaa2', 'col3_name': '4444'})


with open('task07.csv', 'r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['col1_name'], row['col2_name'])


# # Sniffer
# with open('task07.csv', 'r', newline='') as csv_file:
#     dialect = csv.Sniffer().sniff(csv_file.read())
#     print(dialect.delimiter, dialect.quotechar, dialect.quoting)


