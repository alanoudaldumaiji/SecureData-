# SecureData: Data Classification & RBAC

ROLE_PERMISSIONS = {
    "Admin": {"Public", "Internal", "Confidential"},
    "Analyst": {"Public", "Internal"},
    "Viewer": {"Public"}
}

DATA = [
    {
        "name": "Company Website",
        "classification": "Public"
    },
    {
        "name": "Employee Directory",
        "classification": "Internal"
    },
    {
        "name": "Employee Salaries",
        "classification": "Confidential"
    }
]

def check_access(role, classification):
    allowed = ROLE_PERMISSIONS.get(role, set())
    return classification in allowed

print("=== SecureData Access Control Report ===")

for role in ROLE_PERMISSIONS:
    print(f"\nRole: {role}")

    for item in DATA:
        permitted = check_access(
            role,
            item["classification"]
        )

        status = "ALLOWED" if permitted else "DENIED"

        print(f" {item['name']}: {status}")
