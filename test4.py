import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

arquivo = pd.read_excel("Stats.xlsx")

X = ["14/07/22", "15/07/22", "16/07/22",
     "17/07/22", "18/07/22", "19/07/22", "20/07/22"]
Y = [10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6]
Y2 = [-6, 177, 42, 286111]
honor = [177, 1770, 277, 177, 17, 1771, 177]
challenges = [17, 177, 2770, 1779, 17, 1771, 177]
ranking = [170000, 17700, 2770, 1779, 170, 17, 1]
plt.yscale("log")
plt.plot(X, Y, c="w")
plt.plot(X, honor, c="b")
plt.plot(X, challenges, c="r")
plt.plot(X, ranking, c="y")
plt.show()
