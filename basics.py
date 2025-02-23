import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dataset.csv")

data["Autoclicker Used"] = data["Autoclicker Used"].astype(str)

data["Boost Duration"] = pd.to_timedelta(data["Boost Duration"]).dt.total_seconds()

metrics = ["Boost Duration", "Boost Multiplicator", "Count of Taps", "Taps Per Second", "Coins Per Second", "Boost Income"]

overall_stats = data[metrics].describe().T
overall_stats['median'] = data[metrics].median()
print("Overall Descriptive Statistics:\n", overall_stats)

group_stats = data.groupby("Autoclicker Used")[metrics].describe().unstack()
print("\nDescriptive Statistics by Autoclicker Usage:\n", group_stats)

groups = data["Autoclicker Used"].unique()
for group in groups:
    print(f"\nStatistics for Autoclicker Used = {group}:")
    group_data = data[data["Autoclicker Used"] == group][metrics]
    stats = group_data.describe().T
    stats['median'] = group_data.median()
    print(stats)