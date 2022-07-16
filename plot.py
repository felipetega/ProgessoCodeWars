import matplotlib.pyplot as plt
import pandas as pd

# DATASET
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

# FONTS
font1 = {'family': 'serif', 'color': 'darkred', 'size': 20}
font2 = {'family': 'serif', 'color': 'black', 'size': 15}

# PLOT 1
plt.subplot(2, 1, 1)
# STYLE
plt.title("CodeWars", fontdict=font1)
plt.xlabel("Date", fontdict=font2)
plt.ylabel("logarithmic scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
plt.yscale("log")
# DATA
plt.plot(Xdate, Ykyu, c="b")
plt.plot(Xdate, Yhonor, c="r")
plt.plot(Xdate, Ytotal, c="y")
plt.plot(Xdate, Yranking, c="black")

plt.show()
