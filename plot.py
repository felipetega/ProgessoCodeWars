import matplotlib.pyplot as plt
import pandas as pd

x = pd.read_excel("Stats.xlsx")

Xdate = []
Ykyu = []
Yhonor = []
Ytotal = []
Yranking = []

for i in x["Date"]:
     Xdate.append(i)
for i in x["Kyu"]:
    Ykyu.append(i)
for i in x["Honor"]:
  Yhonor.append(i)
for i in x["Total Completed"]:
  Ytotal.append(i)
for i in x["Ranking"]:
  Yranking.append(i)

plt.yscale("log")
plt.plot(Xdate, Ykyu, c="b")
plt.plot(Xdate, Yhonor, c="r")
plt.plot(Xdate, Ytotal, c="y")
#plt.plot(Xdate, Yranking, c="black")
plt.show()
