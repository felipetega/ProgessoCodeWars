import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = np.linspace(-2, 10)
Y = 10**X
plt.yscale("log")
plt.plot(X, Y)
plt.show()
