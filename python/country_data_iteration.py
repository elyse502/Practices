#!/usr/bin/python3
"""
This script demonstrates multiple ways to iterate over a nested Python dictionary.

It uses a dictionary of country representatives to showcase:
- Iteration over dictionary keys, values, and key–value pairs
- Safe data access using dict.get()
- Nested loops for explicit field access
- Enumeration and sorting of dictionary keys
- Dictionary comprehension for data transformation
- Functional-style iteration using map()

The examples are intended for learning and comparison purposes.

Author: Elysée NIYIBIZI
Github: elyse502
"""


country_representative = {
    "Rwanda": {
        "PresidentName": "HE.Paul KAGAME",
        "Role": "country leader",
    },
    "Uganda": {
        "PresidentName": "Museveni",
        "Role": "country leader",
        "number_of_ministries": 12
    },
    "Sudan": {
        "PresidentName": "Omar al-Bashir",
        "Role": "country leader",
        "number_of_ministries": 30
    }
}

# Loop through keys only (default behavior)
for country in country_representative:
    print(country)

print()

for country in country_representative.keys():
    print(country)

print("-" * 40, end="\n\n")

# Loop through values only
for info in country_representative.values():
    print(info)

print("-" * 40, end="\n\n")

# Loop through keys and values
for country, info in country_representative.items():
    print(f"{country:_^10}:")
    for key, value in info.items():
        print(f"\t- {key}: {value}")
    print()

print()

for country, info in country_representative.items():
    print(f"{country:_^10}:")
    print(f"\t- PresidentName: {info.get('PresidentName', 'Unknown')}")
    print(f"\t- Role: {info.get('Role')}")
    if "number_of_ministries" in info:
        print(f"\t- number_of_ministries: {info['number_of_ministries']}")
    print()

print("-" * 40, end="\n\n")

# Nested looping (explicit field access)
for country in country_representative:
    print(f"{country:_^10}:")
    for key in country_representative[country]:
        print(f"\t- {key}: {country_representative[country][key]}")
    print()

print("-" * 40, end="\n\n")

# Using enumerate() (index + key)
for i, country in enumerate(country_representative, start=1):
    print(i, country)

print("-" * 40, end="\n\n")

# Loop with sorted keys
for country in sorted(country_representative):
    print(country)

print()

for country in sorted(country_representative, key=len):
    print(country)

print("-" * 40, end="\n\n")

# Dictionary comprehension (loop + transform)
leaders = {
    country: info["PresidentName"]
    for country, info in country_representative.items()
}
print(leaders)

print("-" * 40, end="\n\n")

# Loop using .items() with unpacking inside
for item in country_representative.items():
    country, info = item
    print(country)

print("-" * 40, end="\n\n")

# Using .get() inside a loop (safe access)
for country, info in country_representative.items():
    print(info.get("PresidentName", "Unknown"))

print("-" * 40, end="\n\n")

# Functional style (map)
for country in map(str.upper, country_representative):
    print(country)

