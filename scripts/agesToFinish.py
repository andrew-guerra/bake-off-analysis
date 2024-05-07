import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/allContestants.csv")

avgAgePerFinish = {}
numFinish = {}

for finish, age in zip(data.Finish, data.Age):
    if not finish in avgAgePerFinish.keys():
        avgAgePerFinish[finish] = age
        numFinish[finish] = 1
    else:
        avgAgePerFinish[finish] += age
        numFinish[finish] += 1

labels = ["Winner", "Runner-up", "4th", "5th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
labels.reverse()
values = [avgAgePerFinish[finish] / numFinish[finish] for finish in labels]

fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_ylabel("Finish")
ax.set_xlabel("Age")
ax.set_title("Average Age Per Finish Place")
plt.savefig("figures/avgAgePerFinishPlace.png")

labels = ["Winner", "Runner-up", "4th", "5th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
labels.sort(key=lambda finish: avgAgePerFinish[finish] / numFinish[finish])
values = [avgAgePerFinish[finish] / numFinish[finish] for finish in labels]

fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_ylabel("Finish")
ax.set_xlabel("Age")
ax.set_title("Average Age Per Finish Place (Sorted)")
plt.savefig("figures/avgAgePerFinishPlaceSorted.png")