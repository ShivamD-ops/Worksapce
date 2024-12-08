import csv
with open('demo/employee.csv','a',newline = '') as file:
    writer = csv.writer(file)
    # writer.writerow(['Name','Age','Job'])
    writer.writerow(['Alex',22,'DEvloper'])
    writer.writerow(['Alen',21,'Tester'])
        
with open('demo/employee.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)








