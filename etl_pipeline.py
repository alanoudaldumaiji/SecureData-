import csv
import sqlite3
from io import StringIO
from pathlib import Path

# EXTRACT: Read fictional employee data
raw_data = """id,name,department
1,Sara,IT
2,Noura,Finance
3,Ahmed,HR
4,Sara,IT
5,,Cybersecurity
6,Maha,Cybersecurity
"""

records = list(csv.DictReader(StringIO(raw_data)))

# TRANSFORM: Remove invalid and duplicate records
clean_records = []
seen = set()
missing = 0
duplicates = 0

for record in records:
    name = record["name"].strip()
    department = record["department"].strip()

    if not name or not department:
        missing += 1
        continue

    key = (name.lower(), department.lower())

    if key in seen:
        duplicates += 1
        continue

    seen.add(key)
    clean_records.append(
        (int(record["id"]), name, department)
    )

# LOAD: Store clean records in SQLite
db_path = Path(__file__).parent / "securedata.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clean_employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

# Refresh the demonstration table on every run
cursor.execute("DELETE FROM clean_employees")

cursor.executemany("""
INSERT INTO clean_employees (id, name, department)
VALUES (?, ?, ?)
""", clean_records)

connection.commit()

# REPORT: Show data quality results
print("=== SecureData ETL Report ===")
print("Original records:", len(records))
print("Missing/invalid records:", missing)
print("Duplicate records:", duplicates)
print("Clean records loaded:", len(clean_records))

cursor.execute("SELECT * FROM clean_employees")
print("\nClean database records:")

for employee in cursor.fetchall():
    print(employee)

connection.close()