import pandas as pd
import matplotlib.pyplot as plt
import parse 

finishValueMap = {
    "Winner": 1,
    "Runner-up": 2.5,
    "4th": 4,
    "5th": 5,
    "6th": 6,
    "7th": 7,
    "8th": 8,
    "9th": 9,
    "10th": 10,
    "11th": 11,
    "12th": 12,
    "13th": 13
}
data = pd.read_csv("data/starBakers.csv")

avgFinishPerWeek = {}
numWeekOccurences = {}

for finish, weeks in zip(data.Finish, data.WeeksWon):
    weeks = list(map(lambda week : parse.search("({})", week)[0], weeks.split(",")))

    for week in weeks:
        if not week in avgFinishPerWeek.keys():
            avgFinishPerWeek[week] = finishValueMap[finish]
            numWeekOccurences[week] = 1
        else:
            avgFinishPerWeek[week] += finishValueMap[finish]
            numWeekOccurences[week] += 1

labels = [key for key in avgFinishPerWeek.keys()]
labels.sort(key=lambda week: avgFinishPerWeek[week] / numWeekOccurences[week])
values = [avgFinishPerWeek[week] / numWeekOccurences[week] for week in labels]

fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_ylabel("Week")
ax.set_xlabel("Finish")
ax.set_title("Average Finish Place Per Star Baker Week (Full)")
plt.savefig("figures/avgFinishPlacePerStarBakerWeekFull.png")

subsetAvgFinishPerWeek = {}
subsetNumWeekOccurences = {}
for week, _ in avgFinishPerWeek.items():
    if numWeekOccurences[week] > 3:
        subsetAvgFinishPerWeek[week] = avgFinishPerWeek[week]
        subsetNumWeekOccurences[week] = numWeekOccurences[week]

labels = [key for key in subsetAvgFinishPerWeek.keys()]
labels.sort(key=lambda week: subsetAvgFinishPerWeek[week] / subsetNumWeekOccurences[week])
values = [subsetAvgFinishPerWeek[week] / subsetNumWeekOccurences[week] for week in labels]

fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_ylabel("Week")
ax.set_xlabel("Finish")
ax.set_title("Average Finish Place Per Star Baker Week (Partial)")
plt.savefig("figures/avgFinishPlacePerStarBakerWeekPartial.png")