import json
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

with open('data.json') as json_file:
    data = json.load(json_file)

x = []
y = []
for a in data["coordinates"]:
    x.append(1920 - a[0])
    y.append(1080 - a[1])

plt.xlim([0, 1920])
plt.ylim([0, 1080])

plt.plot(x, y, 'o', color="red")
plt.show()