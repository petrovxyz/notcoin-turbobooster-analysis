import pandas as pd

data = pd.read_csv("dataset.csv")

data["Autoclicker Used"] = data["Autoclicker Used"].astype(str)

manual_data = data[data["Autoclicker Used"] == "N"]

auto_data = data[data["Autoclicker Used"] == "Y"]

league_counts = manual_data["League"].value_counts()

avg_taps_per_sec = manual_data.groupby("League")["Taps Per Second"].mean()
avg_boost_income_coins = manual_data.groupby("League")["Boost Income"].mean()
avg_boost_income_dollars = (avg_boost_income_coins / 1000) * 0.02896
avg_cpt_before = manual_data.groupby("League")["CPT Before Boost"].mean()
avg_cpt_with = manual_data.groupby("League")["CPT With Boost"].mean()
avg_boost_mult = manual_data.groupby("League")["Boost Multiplicator"].mean()

platinum_manual = manual_data[manual_data["League"] == "Platinum"]
platinum_auto = auto_data[auto_data["League"] == "Platinum"]

avg_taps_platinum_manual = platinum_manual["Taps Per Second"].mean() if not platinum_manual.empty else None
avg_taps_platinum_auto = platinum_auto["Taps Per Second"].mean() if not platinum_auto.empty else None

print("Number of observations for each league (manual play):")
print(league_counts)

print("\nAverage Taps Per Second by League (manual play):")
print(avg_taps_per_sec)

print("\nAverage Boost Income by League (in coins):")
print(avg_boost_income_coins)

print("\nAverage Boost Income by League (in dollars):")
print(avg_boost_income_dollars)

print("\nAverage CPT Before Boost by League:")
print(avg_cpt_before)

print("\nAverage CPT With Boost by League:")
print(avg_cpt_with)

print("\nAverage Boost Multiplicator by League:")
print(avg_boost_mult)

print("\nAverage Taps Per Second in Platinum League:")
print("Manual:", avg_taps_platinum_manual)
print("Autoclicker:", avg_taps_platinum_auto)