import csv

rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

fileOpen = open("CSVWriter.csv", 'w+', newline='\n')
csvWriter = csv.writer(fileOpen)
csvWriter.writerows(rows)

fileOpen.seek(0)
csvReader = csv.reader(fileOpen)
for i in csvReader:
    print(", ".join([k for k in i]))
fileOpen.close()

