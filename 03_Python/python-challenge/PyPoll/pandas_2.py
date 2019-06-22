import pandas as pd
import time
#import collections as clt

import os
input_file = os.path.join("..","Resources","election_data.csv")
start_time = time.time()

# data frame
data = pd.read_csv(input_file)

total = len(data)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

# series (working like a list)
#a = data.groupby('Candidate')['Voter ID'].nunique()
a = data["Candidate"].value_counts()


for i in range(len(a)):
    print(f"{a.index[i]:<11}: {a[i]/total*100.0:7.3f}%  ({a[i]})")

print("-------------------------")
print(f"Winner: {a.idxmax()}")
print("-------------------------")


print("csv.DictReader took %s seconds" % (time.time() - start_time))

