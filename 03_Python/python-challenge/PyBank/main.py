import csv
import time
import numpy as np
import os

input_file = os.path.join("..", "Resources", "budget_data.csv")
start_time = time.time()

data = csv.DictReader(open(input_file))

date = []
pl = []

for row in data:
    date.append(row["Date"])
    pl.append(row["Profit/Losses"])

date = np.asarray(date)
pl = np.asarray(np.int_(pl))

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {date.size}")
print(f"Total: ${np.sum(pl)}")

minChange = float("inf")
maxChange = float("-inf")
sumChange = 0
interval = date.size - 1
for i in range(interval):
    eachChange = pl[i + 1] - pl[i]
    if (minChange > eachChange):
        minChange = eachChange
        minChangeDate = date[i + 1]
    if (maxChange < eachChange):
        maxChange = eachChange
        maxChangeDate = date[i + 1]

    sumChange = sumChange + eachChange

print(f"Average  Change: ${sumChange / interval}")
print(f"Greatest Increase in Profits: ${maxChangeDate} (${maxChange})")
print(f"Greatest Decrease in Profits: ${minChangeDate} (${minChange})")

print("csv.DictReader took %s seconds" % (time.time() - start_time))

text = ((f"Financial Analysis \n-----------------------------\nTotal Months: {date.size} \nTotal: ${np.sum(pl)}  \nAverage  Change: ${sumChange / interval} \nGreatest Increase in Profits: ${maxChangeDate} (${maxChange}) \nGreatest Decrease in Profits: ${minChangeDate} (${minChange})" ))
saveFile = open('PyBank.txt', 'w')
saveFile.write(text)
saveFile.close()
