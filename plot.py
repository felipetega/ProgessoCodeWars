import matplotlib.pyplot as plt
import pandas as pd

# DATASET
x = pd.read_excel("Stats.xlsx")

Xdate = []
Ykyu = []
Ylevel = []
Yhonor = []
YtotalCompleted = []
Yranking = []

for i in x["Date"]:
    Xdate.append(i)
for i in x["Kyu"]:
    Ykyu.append(i)
for i in x["Level"]:
    Ylevel.append(i)
for i in x["Honor"]:
    Yhonor.append(i)
for i in x["Total Completed"]:
    YtotalCompleted.append(i)
for i in x["Ranking"]:
    Yranking.append(i)

# FONTS
font1 = {'family': 'serif', 'color': 'darkred', 'size': 20}
font2 = {'family': 'serif', 'color': 'black', 'size': 15}

# PLOT 1
plt.subplot(2, 2, 1)
# STYLE
plt.title("Ranking, Challenges and Honor", fontdict=font1)
plt.ylabel("logarithmic scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
plt.yscale("log")
# DATA
plt.bar(Xdate, Ylevel, label="Level")
plt.plot(Xdate, Yhonor, c="r", label="Honor")
plt.plot(Xdate, YtotalCompleted, c="y", label="Codes")
plt.plot(Xdate, Yranking, c="black", label="Ranking")
plt.legend(loc="upper right")
# PLOT 2
plt.subplot(2, 2, 2)
# STYLE
plt.title("Honor per Day", fontdict=font1)
#plt.ylabel("normal scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
# DATA
Xdate2=Xdate[1:]
honorPerDay=[]
for i in range(1,len(Yhonor)):
    honorPerDay.append(Yhonor[i]-Yhonor[i-1])
plt.bar(Xdate2, honorPerDay)

# PLOT 3
plt.subplot(2, 2, 3)
# STYLE
plt.title("Ranking Position", fontdict=font1)
#plt.xlabel("Date", fontdict=font2)
#plt.ylabel("normal scale", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
# DATA
plt.plot(Xdate, Yranking, c="black")

# PLOT 4
plt.subplot(2, 2, 4)
# STYLE
plt.title("Proportion: Honor X Codes", fontdict=font1)
#plt.xlabel("Date", fontdict=font2)
#plt.ylabel("codes", fontdict=font2)
plt.grid(axis='both', color='gray', linestyle='-', linewidth=1)
# DATA

labels = ['Codes', 'Honor']
sumCodes = sum(YtotalCompleted)
sumHonor = sum(Yhonor)
arrCodesHonor = [sumCodes,sumHonor]
plt.pie(arrCodesHonor)
plt.legend(labels, loc="upper right")


# SHOW
plt.show()
