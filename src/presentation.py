import pandas as pd
import os

df = pd.read_csv("data/ingested/race_results.csv")

df["Points"] = pd.to_numeric(df["Points"])

os.makedirs("data/presentation", exist_ok=True)

driver_points = df.groupby("Driver")["Points"].sum().reset_index()
driver_points = driver_points.sort_values(by="Points", ascending=False)

constructor_points = df.groupby("Constructor")["Points"].sum().reset_index()
constructor_points = constructor_points.sort_values(by="Points", ascending=False)

race_winners = df[df["Position"] == 1]

driver_points.to_csv("data/presentation/driver_points.csv", index=False)
constructor_points.to_csv("data/presentation/constructor_points.csv", index=False)
race_winners.to_csv("data/presentation/race_winners.csv", index=False)

print("Presentation files created successfully!")
print(driver_points.head())