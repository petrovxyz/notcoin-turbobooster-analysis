import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("dataset.csv")

data["Autoclicker Used"] = data["Autoclicker Used"].astype(str)

auto_data = data[data["Autoclicker Used"] == "Y"]

league_counts = auto_data["League"].value_counts()
print("League Distribution Among Autoclicker Users")
print(league_counts)