import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("dataset.csv")

data["Boost Multiplicator"] = pd.to_numeric(data["Boost Multiplicator"], errors='coerce')
boost_mult = data["Boost Multiplicator"].dropna()

plt.figure(figsize=(10, 6))
sns.histplot(boost_mult, bins=30, kde=True, color='skyblue', edgecolor='black', stat="density")
plt.title("Histogram and Density Plot of Boost Multiplicator", fontsize=14, fontweight='bold')
plt.xlabel("Boost Multiplicator")
plt.ylabel("Density")
plt.show()