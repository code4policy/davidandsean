import json
import csv

with open('superheroes.json') as f:
    data = json.load(f)

with open('output/superheroes.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    squad_info = {
        'squadName': data['squadName'],
        'homeTown': data['homeTown'],
        'formed': data['formed'],
        'secretBase': data['secretBase'],
        'active': data['active']
    }

    for member in data['members']:
        row = {
            'name': member['name'],
            'age': member['age'],
            'secretIdentity': member['secretIdentity'],
            'powers': ', '.join(member['powers']),
            **squad_info
        }
        writer.writerow(row)

print("Data written to CSV file.")