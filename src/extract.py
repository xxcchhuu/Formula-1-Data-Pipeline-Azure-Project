import requests
import json

all_races = []
offset = 0
limit = 100

while True:
    url = f"https://api.jolpi.ca/ergast/f1/2023/results.json?limit={limit}&offset={offset}"

    response = requests.get(
        url,
        headers={"User-Agent": "Formula1Pipeline/1.0"}
    )

    data = response.json()

    races = data["MRData"]["RaceTable"]["Races"]

    if not races:
        break

    all_races.extend(races)

    offset += limit

print("Total races:", len(all_races))

with open("data/raw/f1_results.json", "w") as f:
    json.dump(
        {"MRData": {"RaceTable": {"Races": all_races}}},
        f,
        indent=4
    )