import pandas as pd

data = pd.read_csv("dataset.csv")

data["Autoclicker Used"] = data["Autoclicker Used"].astype(str)

manual_data = data.loc[data["Autoclicker Used"] == "N"]
auto_data   = data.loc[data["Autoclicker Used"] == "Y"]

manual_max_idx = manual_data["Boost Income"].idxmax()
auto_max_idx   = auto_data["Boost Income"].idxmax()

manual_row = manual_data.loc[manual_max_idx]
auto_row   = auto_data.loc[auto_max_idx]

manual_min_idx = manual_data["Boost Income"].idxmin()
auto_min_idx   = auto_data["Boost Income"].idxmin()

manual_worst_row = manual_data.loc[manual_min_idx]
auto_worst_row   = auto_data.loc[auto_min_idx]

relevant_cols = [
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

manual_income_dollars = (manual_row["Boost Income"] / 1000) * 0.02896
auto_income_dollars   = (auto_row["Boost Income"] / 1000)   * 0.02896

manual_income_dollars = (manual_worst_row["Boost Income"] / 1000) * 0.02896
auto_income_dollars   = (auto_worst_row["Boost Income"] / 1000)   * 0.02896

print("Best case without autoclicker")
print(manual_row[relevant_cols])
print(f"Boost Income in $ ($0.02896): {manual_income_dollars:.4f}\n")

print("Best case with autoclicker")
print(auto_row[relevant_cols])
print(f"Boost Income in $ ($0.02896): {auto_income_dollars:.4f}\n")

print("Worst case without autoclicker")
print(manual_worst_row[relevant_cols])
print(f"Boost Income in $ ($0.02896): {manual_income_dollars:.4f}\n")

print("Worst case with autoclicker")
print(auto_worst_row[relevant_cols])
print(f"Boost Income in $ ($0.02896): {auto_income_dollars:.4f}")