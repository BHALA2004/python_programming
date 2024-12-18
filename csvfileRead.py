import csv

with open('example.csv',mode='r') as file:

    csv_read = csv.reader(file);

    for row in csv_read:

         print(row)





import csv


with open('newtext.csv',mode='w') as file:

    csv_write = csv.writer(file)

    csv_write.writerow('[name],[age]')

    csv_write.writerow('[bala],[20]')




import json

data = {"name":"Bala","Age":"20"}

with open('jsonOperates.json',mode='w') as file:
    json.dump(data,file)


with open('jsonOperates.json',mode='r') as file:
    content = json.load(file)
    print(content)
