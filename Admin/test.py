import csv

with open('/home/narayanj/Practice/THAR2.0/Admin/participate_events.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    print(len(data[0]))