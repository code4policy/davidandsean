import csv

vegetables = [
    {"name": "eggplant", "color": "purple"},
    {"name": "tomato", "color": "red"},
    {"name": "corn", "color": "yellow"},
    {"name": "okra", "color": "green"},
    {"name": "arugula", "color": "green"},
    {"name": "broccoli", "color": "green"},
]

with open('vegetables.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])  # Write the header

    for veggie in vegetables:
        writer.writerow([veggie['name'], veggie['color']])  # Write each vegetable's name and color

