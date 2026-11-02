import csv

with open ("Study_Area_Wards.csv", encoding = "utf-8-sig") as f:
    reader = csv.DictReader (f)
    rows = list (reader)
print ("Number of rows:", len (rows))
print ("columns:", list(rows [0].keys()))

import csv

with open ("Study_Area_Wards.csv", encoding = "utf-8-sig") as f:
    rows = list (csv.DictReader (f))

values = []
for row in rows:
    value = float(row ["area_km2"])
    values.append (value)

print ("Smallest:", min (values))
print ("Largest", max(values))
print ("Count:", len (values))

import csv
with open ("Study_Area_Wards.csv", encoding = "utf-8-sig") as f:
    rows = list (csv.DictReader (f))

values =[]
for row in rows:
    raw = row ["area_km2"].strip ()
    if raw =="":
        continue
    values.append (float(raw))
print ("Smallest:", min (values))
print ("Largest:", max (values))
print ("count:", len (values))

import csv
def inspect_column (Study_Area_Wards, area_km2):
    with open (Study_Area_Wards, encoding = "utf-8-sig") as f:
        rows = list (csv.DictReader (f))

    values = []
    for row in rows:
        raw = row [area_km2].strip()
        if raw == "":
            continue
        values.append (float(raw))

    return {
        "Smallest": min (values),
        "Largest": max (values),
        "count": len (values),
    }
result = inspect_column ("Study_Area_Wards.csv", "area_km2")
print (result)
