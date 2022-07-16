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
plt.subplot(2, 2, 1)
# STYLE
plt.title("All Data", fontdict=font1)
plt.ylabel("logarithmic scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
plt.yscale("log")
# DATA
plt.plot(Xdate, Ykyu, c="b")
plt.plot(Xdate, Yhonor, c="r")
plt.plot(Xdate, Ytotal, c="y")
plt.plot(Xdate, Yranking, c="black")

# PLOT 2
plt.subplot(2, 2, 2)
# STYLE
plt.title("Kyu, Challenges and Honor", fontdict=font1)
plt.ylabel("normal scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
# DATA
plt.plot(Xdate, Ykyu, c="b")
plt.plot(Xdate, Yhonor, c="r")
plt.plot(Xdate, Ytotal, c="y")

# PLOT 3
plt.subplot(2, 2, 3)
# STYLE
plt.title("Ranking Position", fontdict=font1)
plt.xlabel("Date", fontdict=font2)
plt.ylabel("normal scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
# DATA
plt.plot(Xdate, Yranking, c="black")

# PLOT 4
plt.subplot(2, 2, 4)
# STYLE
plt.title("Completed Challenges", fontdict=font1)
plt.xlabel("Date", fontdict=font2)
plt.ylabel("normal scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
# DATA
plt.plot(Xdate, Ytotal, c="y")

# SHOW
plt.show()
