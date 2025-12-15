import matplotlib.pyplot as plt
import numpy as np

file = open("opendata.stat", "r", encoding="utf-8")
s = file.readlines()

date_data = np.array([])
money_data = np.array([])

count = 0
summa = 0
for line in s:
    line = line.split(",")
    if line[0] == "Средняя пенсия" and line[1] == "Забайкальский край" and line[2][:4] == "2018":
        count += 1
        summa += int(line[3])
        date_data = np.append(date_data, [line[2]])
        money_data = np.append(money_data, int(line[3]))

print(summa/count)


plt.plot(date_data, money_data)
plt.xlabel("Дата")
plt.ylabel("Средняя пенсия")

plt.show()
