

import csv
import json

vegetables = []

with open('output/vegetables.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        vegetables.append({"name": row["name"], "color": row["color"]})

with open('output/vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=2)