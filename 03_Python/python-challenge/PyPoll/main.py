import csv
import time 
import numpy as np
import pandas as pd
import os

input_file = os.path.join("..","Resources","election_data.csv")
start_time = time.time()

csvframe = pd.read_csv(input_file)

#print(csvframe.head())

#access the 'Voter ID' column and call the groupby() function with the Candidate column
group= csvframe[['Voter ID']].groupby(csvframe['Candidate'])

#Counting Vote by Candidate
countVote= group.count()
percentVote= group.count()/(csvframe['Voter ID'].count())*100
print("============= Election Result=============")

print(f" Total Votes: {csvframe['Voter ID'].count()}")
print("------------------------------------------")
print (countVote)
print("------------------------------------------")
print( percentVote)
print("------------------------------------------")

final_result=pd.merge(percentVote,countVote,on="Candidate")
final_result.rename(columns={'Voter ID_x': 'Percentage','Voter ID_y':'Number of Vote'}, inplace=True)
print(final_result.sort_values(by=['Percentage'],ascending=False))
#print(type(final_result))
#print(final_result.sort_values(by=['Percentage'],ascending=False))
print("------------------------------------------")
print(countVote.idxmax())
print(f"Running time: {time.time() - start_time}")