import csv
with open('yellow_tripdata_2020-01.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)