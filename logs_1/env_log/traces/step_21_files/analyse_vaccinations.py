import pandas as pd


df = pd.read_csv("us_state_vaccinations.csv")
df = df[df["date"] == "2023-05-10"]


relevant_data = df[["location", "people_fully_vaccinated_per_hundred", "total_vaccinations_per_hundred", "daily_vaccinations_per_million"]]
print(relevant_data.columns)
print(relevant_data.head())

mean = relevant_data["people_fully_vaccinated_per_hundred"].mean()
print(mean)
median = relevant_data["people_fully_vaccinated_per_hundred"].median()  
print(median)