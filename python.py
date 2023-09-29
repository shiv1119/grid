import csv
import matplotlib.pyplot as plt;

label = []
droupout = []
with open('DOR.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['State_UT'] == 'Uttar Pradesh':
            label.append(row['year'])
            droupout.append(row['Primary_Total'])
            
            


plt.pie(droupout, labels=label)