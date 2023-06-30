import os
import sys
import pandas as pd


working = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(working)
txtout = os.path.join(working,'analysis','output.txt')
results = open(txtout,'w')
csvin = os.path.join(working,'resources','budget_data.csv')
sys.stdout = results
data= pd.read_csv(csvin)
data['Difference']=data["Profit/Losses"].diff()
print('Financial Analysis')
print('----------------------------')
print('Total Months: ',len(data.index),sep='')
print('Total: $',data.sum()[1],sep='')
print('Average Change: $',round(data["Profit/Losses"].diff().mean(numeric_only=True),2),sep='')
print('Greatest increase in profits: ',data['Date'].iloc[(int(data['Difference'].idxmax(skipna=True)))],' ($',round(data['Difference'].max(numeric_only=True)),')',sep='')
print('Greatest decrease in profits: ',data['Date'].iloc[(int(data['Difference'].idxmin(skipna=True)))],' ($',round(data['Difference'].min(numeric_only=True)),')',sep='')
results.close()