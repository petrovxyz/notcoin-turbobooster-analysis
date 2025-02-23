import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("your_data.csv")

data["Autoclicker Used"] = data["Autoclicker Used"].astype(str)

auto_data = data[data["Autoclicker Used"] == "Y"]

league_counts = auto_data["League"].value_counts()
print("=== League Distribution Among Autoclicker Users ===")
print(league_counts)

plt.figure(figsize=(8, 4))
sns.countplot(x="League", data=auto_data, order=league_counts.index, palette="viridis")
plt.title("League Distribution Among Autoclicker Users", fontsize=14, fontweight="bold")
plt.xlabel("League")
plt.ylabel("Count of Players")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()