import csv
import time
import collections as clt
import os


input_file = os.path.join("..","Resources","election_data.csv")
#input_file = "/Users/zacharyvunguyen/Documents/GitHub/DataAnalytic/03_Python/python-challenge/Resources/election_data.csv"
start_time = time.time()

data = csv.DictReader(open(input_file))

cand = []

for row in data:
    cand.append(row["Candidate"])

total = len(cand)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

# dictionary of candidates and their votes
thisdict = clt.Counter(cand)

ymax = 0
for x, y in thisdict.items():
  print(f"{x:<11}: {y/total*100.0:7.3f}%  ({y})")
  if ymax<y:
      ymax = y
      xmax = x

#------------------------
loopOutput=[]
ymax = 0
for x, y in thisdict.items():
  #print(f"{x:<11}: {y/total*100.0:7.3f}%  ({y})")
  loopOutput.append(f"{x:<11}: {y/total*100.0:7.3f}%  ({y})")
  if ymax<y:
      ymax = y
      xmax = x
loopOutput='\n'.join(loopOutput) #add new line to list

print("-------------------------")
print(f"Winner: {xmax}")
print("-------------------------")

print("csv.DictReader took %s seconds" % (time.time() - start_time))

text = ((f"Election Results \n-----------------------------\nTotal Votes: {total} \n----------------------------- \n{loopOutput} \n----------------------------- \nWinner: {xmax}   " ))
saveFile = open('PyPoll.txt', 'w')
saveFile.write(text)
saveFile.close()
