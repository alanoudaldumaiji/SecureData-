import sqlite3
from pathlib import Path

# Connect to the database
db_path = Path(__file__).parent / "securedata.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create the employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

# Sample fictional employee records
employees = [
    (1, "Sara", "IT"),
    (2, "Noura", "Finance"),
    (3, "Ahmed", "HR"),
    (4, "Sara", "IT"),
    (5, "Maha", "Cybersecurity")
]

# Insert data without duplicating IDs on reruns
cursor.executemany("""
INSERT OR IGNORE INTO employees (id, name, department)
VALUES (?, ?, ?)
""", employees)

connection.commit()

# Query the database
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()

print("=== SecureData: SQL Database ===")
for employee in results:
    print(employee)

print("Total records in database:", len(results))

connection.close()
