import csv

csv.register_dialect('my_dialect', delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
# print(csv.list_dialects())


with open('task07.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['qqq1', 'qqq2', '2222'])

with open('task07.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, 'my_dialect')
    for row in reader:
        print(row[0])

