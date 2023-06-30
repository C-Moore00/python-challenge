import os
import sys
import pandas as pd
import numpy as np

working = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(working)
txtout = os.path.join(working,'analysis','output.txt')
results = open(txtout,'w')
csvin = os.path.join(working,'resources','election_data.csv')
sys.stdout = results
data= pd.read_csv(csvin)
winvote = 1
print('Election Results')
print('-------------------------')
totalvotes = int(len(data.index))
print('Total Votes: ',totalvotes,sep='')
print('-------------------------')
Candidates=data['Candidate'].unique()
#print(Candidates)
for i in Candidates:
    votes = int(data['Candidate'].value_counts(sort=False)[int(np.where(Candidates == i)[0])])
    print(i,': ',100*round(votes/totalvotes,5),'% (',votes,')',sep='')
    if votes > winvote:
        winvote = votes
        winner = i
print('-------------------------')
print('Winner: ',winner)
print('-------------------------')
results.close()