import matplotlib.pyplot as plt
import csv

keys = {}

with open('keebor-log.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        keys[row[0]] = row[1]

keys = {key: val for key, val in sorted(keys.items(), key = lambda ele: ele[1])}

plt.bar(keys.keys(), keys.values())
plt.ylim(ymin=0)
plt.show()
