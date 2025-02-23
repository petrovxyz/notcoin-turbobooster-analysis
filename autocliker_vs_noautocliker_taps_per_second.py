import pandas as pd

data = pd.read_csv("dataset.csv")

data["Autoclicker Used"] = data["Autoclicker Used"].astype(str)

manual_data = data[data["Autoclicker Used"] == "N"]
auto_data   = data[data["Autoclicker Used"] == "Y"]

manual_best_idx = manual_data["Taps Per Second"].idxmax()
auto_best_idx   = auto_data["Taps Per Second"].idxmax()

manual_best = manual_data.loc[manual_best_idx]
auto_best   = auto_data.loc[auto_best_idx]

manual_worst_idx = manual_data["Taps Per Second"].idxmin()
auto_worst_idx   = auto_data["Taps Per Second"].idxmin()

manual_worst = manual_data.loc[manual_worst_idx]
auto_worst   = auto_data.loc[auto_worst_idx]

columns = [
    "Date",
    "League", 
    "Boost Duration",
    "CPT Before Boost", 
    "Multitap LVL", 
    "Boost Multiplicator", 
    "CPT With Boost", 
    "Taps Per Second", 
    "Coins Per Second", 
    "Boost Income", 
    "Energy Limit"
]

manual_best_income = (manual_best["Boost Income"] / 1000) * 0.02896
auto_best_income   = (auto_best["Boost Income"]   / 1000) * 0.02896
manual_worst_income = (manual_worst["Boost Income"] / 1000) * 0.02896
auto_worst_income   = (auto_worst["Boost Income"]   / 1000) * 0.02896

print("Best case without autoclicker by Taps Per Second")
print(manual_best[columns])
print("Boost Income in $: {:.4f}".format(manual_best_income))
print("\nBest case with autoclicker by Taps Per Second")
print(auto_best[columns])
print("Boost Income in $: {:.4f}".format(auto_best_income))

print("Worst case without autoclicker by Taps Per Second")
print(manual_worst[columns])
print("Boost Income in $: {:.4f}".format(manual_worst_income))
print("\nWorst case with autoclicker by Taps Per Second")
print(auto_worst[columns])
print("Boost Income in $: {:.4f}".format(auto_worst_income))
