# Notcoin Turbo Booster Analysis

## A Data-Driven Analysis of Boosters, Multitap Levels, and Economic Efficiency in Notcoin

This repository contains Python scripts for analyzing the **turbo booster mechanics in Notcoin**, focusing on **multitap levels, energy limits, and payback periods**. Using real gameplay data, **statistical methods, and visualizations**, this project provides **insights into upgrade efficiency, income optimization, and the role of autoclickers in gameplay**.

---

## 📌 Features

✔️ **Descriptive Statistics** – Compute fundamental gameplay metrics (mean, median, min, max, std)  
✔️ **Autoclicker vs. Manual Analysis** – Compare performance across tapping speed, boost income, and efficiency  
✔️ **League Distributions** – Explore how leagues impact player income and engagement  
✔️ **Boost Multiplicator Randomness Check** – Perform statistical tests (Chi-Square & Kolmogorov-Smirnov)  
✔️ **Upgrade Payback Periods** – Calculate how long it takes for multitap and energy upgrades to pay off  
✔️ **Energy Limit Investigation** – Detect when a game update introduced a boost income cap  

---

## 📂 Structure
┣ 📜 autoclicker_leagues.py – League distribution analysis for autoclickers

┣ 📜 autoclicker_vs_noautoclicker.py – General comparison between manual and autoclicker play

┣ 📜 autoclicker_vs_noautoclicker_boost_income.py – Boost income analysis by tapping method

┣ 📜 autoclicker_vs_noautoclicker_coins_per_second.py – Coins per second comparison

┣ 📜 autoclicker_vs_noautoclicker_taps_per_second.py – Taps per second comparison

┣ 📜 basics.py – Descriptive statistics for key game variables

┣ 📜 daily_excess_ratio.csv – Data for energy limit impact detection

┣ 📜 dataset.csv – The main dataset used for analysis

┣ 📜 goodness-of-fit-test.py – Statistical tests on Boost Multiplicator distribution

┣ 📜 leaguesdistribution_manual.py – League distribution analysis for manual players

┣ 📜 payback.py – Payback period calculations for multitap and energy upgrades

---

## 📥 Installation

### 🔹 Install dependencies
```bash
pip install pandas numpy matplotlib scipy
```
---

### 📄 Read the full research -> [here](https://petrovxyz.notion.site/Back-to-the-Past-Notcoin-s-Turbo-Booster-A-Data-Driven-Analysis-198697ae15e98074b258d0d26e26a343)

---

### 💬 Contact
▫️ [Telegram](https://t.me/petrovxyz)

▫️ [X](https://x.com/petrovxyz)
