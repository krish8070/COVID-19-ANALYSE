# covid_analysis.py

# 📦 Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# 📁 Load Dataset
file_path = "data/covid-data.csv"  # Ensure the CSV is in this path
df = pd.read_csv(file_path)

# 🧹 Basic Data Exploration
print("\n--- Dataset Info ---")
df.info()

print("\n--- Null Values ---")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\n--- Columns ---")
print(df.columns.tolist())

# 🗃️ Select Columns of Interest
columns_needed = [
    'location', 'date', 'total_cases', 'new_cases', 'total_deaths',
    'new_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'
]
df = df[columns_needed]

# 🧪 Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# 🌍 Filter for a Specific Country (e.g., India)
country = 'India'
df_country = df[df['location'] == country].copy()

# 📈 Plot 1: Total Cases Over Time
plt.figure()
sns.lineplot(data=df_country, x='date', y='total_cases')
plt.title(f"Total COVID-19 Cases Over Time in {country}")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📉 Plot 2: New Cases Over Time
plt.figure()
sns.lineplot(data=df_country, x='date', y='new_cases', color='orange')
plt.title(f"Daily New COVID-19 Cases in {country}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 💉 Plot 3: Vaccination Progress
plt.figure()
sns.lineplot(data=df_country, x='date', y='people_vaccinated', label='People Vaccinated')
sns.lineplot(data=df_country, x='date', y='people_fully_vaccinated', label='Fully Vaccinated')
plt.title(f"COVID-19 Vaccination Progress in {country}")
plt.xlabel("Date")
plt.ylabel("People Vaccinated")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ⚰️ Plot 4: Daily Deaths
plt.figure()
sns.lineplot(data=df_country, x='date', y='new_deaths', color='black')
plt.title(f"Daily New COVID-19 Deaths in {country}")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 Plot 5: Case Fatality Rate (%)
df_country['case_fatality_rate'] = (df_country['total_deaths'] / df_country['total_cases']) * 100

plt.figure()
sns.lineplot(data=df_country, x='date', y='case_fatality_rate', color='red')
plt.title(f"Case Fatality Rate (%) Over Time in {country}")
plt.xlabel("Date")
plt.ylabel("Fatality Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🧮 Plot 6: Vaccination Coverage (Assuming India's population)
population = 1_400_000_000  # Update this if needed
df_country['vaccinated_pct'] = (df_country['people_vaccinated'] / population) * 100
df_country['fully_vaccinated_pct'] = (df_country['people_fully_vaccinated'] / population) * 100

plt.figure()
sns.lineplot(data=df_country, x='date', y='vaccinated_pct', label='At least one dose')
sns.lineplot(data=df_country, x='date', y='fully_vaccinated_pct', label='Fully vaccinated')
plt.title(f"COVID-19 Vaccination Coverage (%) in {country}")
plt.xlabel("Date")
plt.ylabel("Coverage (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# ✅ Summary
print(f"\n--- Latest Stats for {country} ---")
latest = df_country.sort_values('date').dropna(subset=['total_cases']).iloc[-1]
print(latest[['date', 'total_cases', 'total_deaths', 'people_vaccinated', 'people_fully_vaccinated']])
