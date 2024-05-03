import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

rows = []
with open('data/allcontestants.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

startBakers = {}
placeTotals = {}
for i in range(len(rows)):
    if i == 0 or rows[i][5] == "NA":
        continue
    
    if not rows[i][6] in startBakers.keys():
        startBakers[rows[i][6]] = int(rows[i][5])
        placeTotals[rows[i][6]] = 1
    else:
        startBakers[rows[i][6]] += int(rows[i][5])
        placeTotals[rows[i][6]] += 1

labels = ["Winner", "Runner-up", "4th", "5th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
labels.reverse()

agesValues = [startBakers[key] / placeTotals[key] for key in labels]

fig, ax = plt.subplots()
ax.barh(labels, agesValues)
ax.set_ylabel("Finish")
ax.set_xlabel("Star Bakers")
ax.set_title("Average Number of Star Bakers Per Finish Place")
plt.savefig("figures/starBakerAvgPerFinish.png")