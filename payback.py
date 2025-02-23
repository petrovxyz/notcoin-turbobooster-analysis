import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

def time_to_seconds(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
        elif len(parts) == 2:
            hours = 0
            minutes, seconds = map(int, parts)
        elif len(parts) == 1:
            hours = 0
            minutes = 0
            seconds = int(parts[0])
        else:
            return None
        return hours * 3600 + minutes * 60 + seconds
    except (ValueError, TypeError):
        return None

df['Boost Duration (seconds)'] = df['Boost Duration'].apply(time_to_seconds)
df.dropna(subset=['Boost Duration (seconds)'], inplace=True)
df['Boost Duration (seconds)'] = df['Boost Duration (seconds)'].astype(int)

ATH_price = 0.02896
df['Boost Income ($)'] = (df['Boost Income'] / 1000) * ATH_price

multitap_data = {
    'Level': list(range(16)),
    'Price': [0, 100, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000, 2048000, 4096000, 8192000, 16384000],
    'CPT Before Boost': list(range(1, 17))
}
multitap_df = pd.DataFrame(multitap_data)
multitap_df['Price ($)'] = (multitap_df['Price'] / 1000) * ATH_price

energy_limit_data = {
    'Level': list(range(16)),
    'Price': [0, 100, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000, 2048000, 4096000, 8192000, 16384000],
    'Energy Limit': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500]
}
energy_limit_df = pd.DataFrame(energy_limit_data)
energy_limit_df['Price ($)'] = (energy_limit_df['Price'] / 1000) * ATH_price

multitap_avg = df.groupby("CPT Before Boost")["Boost Income"].mean().reset_index()
multitap_avg.rename(columns={"Boost Income": "Avg Boost Income (Notcoin)"}, inplace=True)
multitap_avg_usd = df.groupby("CPT Before Boost")["Boost Income ($)"].mean().reset_index()
multitap_avg_usd.rename(columns={"Boost Income ($)": "Avg Boost Income ($)"}, inplace=True)

multitap_merged = pd.merge(multitap_df, multitap_avg, on="CPT Before Boost", how="left")
multitap_merged = pd.merge(multitap_merged, multitap_avg_usd, on="CPT Before Boost", how="left")

energy_avg = df.groupby("Energy Limit")["Boost Income"].mean().reset_index()
energy_avg.rename(columns={"Boost Income": "Avg Boost Income (Notcoin)"}, inplace=True)
energy_avg_usd = df.groupby("Energy Limit")["Boost Income ($)"].mean().reset_index()
energy_avg_usd.rename(columns={"Boost Income ($)": "Avg Boost Income ($)"}, inplace=True)

energy_merged = pd.merge(energy_limit_df, energy_avg, on="Energy Limit", how="left")
energy_merged = pd.merge(energy_merged, energy_avg_usd, on="Energy Limit", how="left")

def calculate_payback_level(merged_df, boosters_per_day):

    merged_df['Daily Income (Notcoin)'] = merged_df["Avg Boost Income (Notcoin)"] * boosters_per_day
    merged_df['Daily Income ($)'] = merged_df["Avg Boost Income ($)"] * boosters_per_day
    merged_df['Payback (Days)'] = merged_df['Price'] / merged_df['Daily Income (Notcoin)']
    merged_df['Payback (Days)'] = merged_df['Payback (Days)'].replace([np.inf, -np.inf], np.nan).round().astype('Int64')
    return merged_df

boosts_per_day = 6 

boost_duration = 10 

med_cps_noac = df[df["Autoclicker Used"] == "N"]["Coins Per Second"].median()
med_cps_ac = df[df["Autoclicker Used"] == "Y"]["Coins Per Second"].median()
med_cps_overall = df["Coins Per Second"].median()

med_cps_noac_dollar = (med_cps_noac / 1000) * ATH_price
med_cps_ac_dollar = (med_cps_ac / 1000) * ATH_price
med_cps_overall_dollar = (med_cps_overall / 1000) * ATH_price

print("\nMedian Coins Per Second:")
print(f"Manual (No AC): {med_cps_noac:.2f} coins/sec, {med_cps_noac_dollar:.4f} $/sec")
print(f"With AC: {med_cps_ac:.2f} coins/sec, {med_cps_ac_dollar:.4f} $/sec")
print(f"Overall: {med_cps_overall:.2f} coins/sec, {med_cps_overall_dollar:.4f} $/sec")

results = []
for level in range(16):
    cpt = level + 1
    income_per_booster_noac = med_cps_noac * boost_duration * cpt
    daily_income_noac = income_per_booster_noac * boosts_per_day

    income_per_booster_ac = med_cps_ac * boost_duration * cpt
    daily_income_ac = income_per_booster_ac * boosts_per_day

    results.append({
        "Level": level,
        "CPT Before Boost": cpt,
        "Price (coins)": multitap_df.loc[multitap_df["Level"] == level, "Price"].values[0],
        "Income per Booster (No AC, coins)": round(income_per_booster_noac, 2),
        "Daily Income (No AC, coins)": round(daily_income_noac, 2),
        "Income per Booster (AC, coins)": round(income_per_booster_ac, 2),
        "Daily Income (AC, coins)": round(daily_income_ac, 2)
    })

multitap_income_df = pd.DataFrame(results)

multitap_income_df["Daily Income (No AC, $)"] = (multitap_income_df["Daily Income (No AC, coins)"] / 1000) * ATH_price
multitap_income_df["Daily Income (AC, $)"] = (multitap_income_df["Daily Income (AC, coins)"] / 1000) * ATH_price

multitap_income_df["Payback (No AC, Days)"] = multitap_income_df["Price (coins)"] / multitap_income_df["Daily Income (No AC, coins)"]
multitap_income_df["Payback (AC, Days)"] = multitap_income_df["Price (coins)"] / multitap_income_df["Daily Income (AC, coins)"]

multitap_income_df["Payback (No AC, Days)"] = multitap_income_df["Payback (No AC, Days)"].round(1)
multitap_income_df["Payback (AC, Days)"] = multitap_income_df["Payback (AC, Days)"].round(1)

print("\nDaily Income and Payback for Each Multitap Level Based on Median Coins Per Second:")
print(multitap_income_df)