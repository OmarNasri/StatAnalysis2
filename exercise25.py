import pandas as pd
from scipy.stats import shapiro
import matplotlib.pyplot as plt

url = "https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt"

columns = ["Year", "No_Smoothing", "Lowess(5)"]
df = pd.read_csv(url, skiprows=5, sep="\s+", names=columns)


#mean and median for the variable No_Smoothing
mean = df["No_Smoothing"].mean()
median = df["No_Smoothing"].median()

print("Mean: ", mean)
print("Median: ", median)

#check if the variable No_Smoothing is normally distributed
def is_normal(data):
    if shapiro(data)[1] > 0.05:
        return True
    else:
        return False
print("Is the variable No_Smoothing normally distributed? ", is_normal(df["No_Smoothing"]))

plt.hist(df["No_Smoothing"], color='blue', bins=10)
plt.show()

#check if variable no_smoothing is normally distributed but only from year 2000 onwards
df2 = df[df["Year"] >= 2000]
print("Is the variable No_Smoothing normally distributed from year 2000 onwards? ", is_normal(df2["No_Smoothing"]))

plt.hist(df2["No_Smoothing"], color='blue', bins=4)
plt.show()