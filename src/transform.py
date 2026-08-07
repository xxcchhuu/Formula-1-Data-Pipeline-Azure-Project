import json
import pandas as pd

with open("data/raw/f1_results.json", "r") as f:
    data = json.load(f)

races = data["MRData"]["RaceTable"]["Races"]

records = []

for race in races:
    race_name = race["raceName"]

    for result in race["Results"]:
        driver = (
            result["Driver"]["givenName"]
            + " "
            + result["Driver"]["familyName"]
        )

        constructor = result["Constructor"]["name"]

        records.append({
            "Race": race_name,
            "Driver": driver,
            "Constructor": constructor,
            "Position": result["position"],
            "Points": result["points"]
        })

df = pd.DataFrame(records)

print("Total races:", len(races))
print("Total records:", len(records))
print("Unique races:", len(df["Race"].unique()))

df.to_csv(
    "data/ingested/race_results.csv",
    index=False
)

print(df.head())
print("CSV created successfully!")