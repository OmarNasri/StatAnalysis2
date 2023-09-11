import numpy as np
from scipy.stats import shapiro
import matplotlib.pyplot as plt
import seaborn as sns

heights1 = np.array([170, 192, 184, 168, 176, 181, 163])
heights2 = np.array([170, 170, 170, 170, 192, 192, 192, 192, 184, 184, 184, 184, 168, 168, 168, 168, 176, 176,
176, 176, 181, 181, 181, 181, 163, 163, 163, 163 ])

def is_normal(data):
    if shapiro(data)[1] > 0.05:
        return True
    else:
        return False
    
print(is_normal(heights1))
print(is_normal(heights2))

#create histogram plots
plt.hist(heights2, color='blue', bins=4)
plt.hist(heights1, color='red', bins=4)
plt.show()

#create density plots with seaborn
sns.distplot(heights1, hist=False, color='red')
sns.distplot(heights2, hist=False, color='blue')
plt.show()

