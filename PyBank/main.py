import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvpath = csv.reader(csvfile, delimiter=",")
    next(csvpath)
    revenue = []
    date = []
    rev_change = []
    
    for row in csvpath:
        revenue.append(float(row[1]))
        date.append(row[0])

print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(date))
print("Total Revenue: $", sum(revenue))

for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


print("Avereage Revenue Change: $", round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

