import csv
from io import StringIO

# Sample fictional company data
data = """id,name,department
1,Sara,IT
2,Noura,Finance
3,Ahmed,HR
4,Sara,IT
5,,Cybersecurity
"""

employees = list(csv.DictReader(StringIO(data)))

print("=== SecureData: Data Quality Report ===")
print("Total records:", len(employees))

missing_names = [
employee for employee in employees
if not employee["name"].strip()
]

print("Records with missing names:", len(missing_names))

seen = set()
duplicates = []

for employee in employees:
    key = (employee["name"], employee["department"])
    if key in seen:
        duplicates.append(employee)
    else:
        seen.add(key)

print("Potential duplicate records:", len(duplicates))
