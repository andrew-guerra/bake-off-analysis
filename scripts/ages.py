import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

rows = []
with open('data/allcontestants.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

agesSeries = {}
seriesTotals = {}
for i in range(len(rows)):
    if i == 0:
        continue
    
    if not rows[i][4] in agesSeries.keys():
        agesSeries[rows[i][4]] = 0
        seriesTotals[rows[i][4]] = 1
    else:
        agesSeries[rows[i][4]] += int(rows[i][1])
        seriesTotals[rows[i][4]] += 1

labels = [key for key in agesSeries.keys()]
agesValues = [agesSeries[key] / seriesTotals[key] for key in agesSeries.keys()]

fig, ax = plt.subplots()
ax.barh(labels, agesValues)
ax.set_ylabel("Series")
ax.set_xlabel("Age")
ax.set_title("Average Age of Bakers Per Series")
plt.savefig("figures/ages.png")

labels = [key for key in agesSeries.keys()]
labels.sort(key=lambda key: agesSeries[key] / seriesTotals[key])
agesValues = [agesSeries[key] / seriesTotals[key] for key in labels]

fig, ax = plt.subplots()
ax.barh(labels, agesValues)
ax.set_ylabel("Series")
ax.set_xlabel("Age")
ax.set_title("Average Age of Bakers Per Series (Sorted)")
plt.savefig("figures/agesSorted.png")