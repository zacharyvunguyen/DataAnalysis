import csv

with open('Daily/Resources/cereal.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)
    
    for row in readCSV:
        if float(row[7]) >=5:
            print (f"{row[0]}   {row[7]}")
       



