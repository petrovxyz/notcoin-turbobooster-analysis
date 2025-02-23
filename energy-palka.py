import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset.csv")

data["Date"] = pd.to_datetime(data["Date"])

data["Boost Income"] = pd.to_numeric(data["Boost Income"], errors="coerce")
data["Energy Limit"] = pd.to_numeric(data["Energy Limit"], errors="coerce")

data["Excess"] = data["Boost Income"] - data["Energy Limit"]

data["YearMonthDay"] = data["Date"].dt.to_period("D")

daily_excess = data.groupby("YearMonthDay")["Excess"].apply(lambda x: (x > 0).sum())
daily_total = data.groupby("YearMonthDay")["Excess"].count()
daily_ratio = daily_excess / daily_total

daily_ratio_df = daily_ratio.reset_index()
daily_ratio_df.columns = ["Date", "Proportion"]

print("Proportion of observations where Boost Income exceeds Energy Limit by day:")
print(daily_ratio_df)

daily_ratio_df.to_csv("daily_excess_ratio.csv", index=False)
print("The table has been exported to 'daily_excess_ratio.csv'.")

excess_cases = data[data["Excess"] > 0]
last_excess_date = excess_cases["Date"].max()
print("Last observed date with Boost Income > Energy Limit:", last_excess_date)