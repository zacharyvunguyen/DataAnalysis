import csv
import time
import numpy as np
import os
input_file = os.path.join("..","Resources","budget_data.csv")

start_time = time.time()

data = csv.DictReader(open(input_file))


date =[]
pl = []

for row in data:
    date.append(row["Date"])
    pl.append(row["Profit/Losses"])

date = np.asarray(date)
pl = np.asarray(np.int_(pl))

# array of differences
pl1 = np.zeros(pl.size)
pl1[:-1]=pl[1:]
pl1[-1]=pl[-1]
pl1= pl1-pl

# get man/min values
maxChange = np.max(pl1)
maxChangeDate = date[np.where(pl1 == maxChange)[0]+1]
minChange = np.min(pl1)
minChangeDate = date[np.where(pl1 == minChange)[0]+1]

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {date.size}")
print(f"Total: ${np.sum(pl)}")
print(f"Average  Change: ${np.sum(pl1)/(pl1.size-1)}")
print(f"Greatest Increase in Profits: ${maxChangeDate} (${maxChange})")
print(f"Greatest Decrease in Profits: ${minChangeDate} (${minChange})")

print("csv.DictReader took %s seconds" % (time.time() - start_time))

text = ((f"Financial Analysis \n-----------------------------\nTotal Months: {date.size} \nTotal: ${np.sum(pl)}  \nAverage  Change: ${np.sum(pl1)/(pl1.size-1)} \nGreatest Increase in Profits: ${maxChangeDate} (${maxChange}) \nGreatest Decrease in Profits: ${minChangeDate} (${minChange})" ))
saveFile = open('PyBank_main_1.txt', 'w')
saveFile.write(text)
saveFile.close()

