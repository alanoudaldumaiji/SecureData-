# SecureData
### Enterprise Data Security & Governance

An independent Python and SQL project demonstrating data quality validation, ETL processing, role-based access control (RBAC), and automated security testing.

## Project Overview

Organizations need reliable data processing and appropriate access controls to protect sensitive information.

SecureData demonstrates a small-scale approach to identifying data quality issues, storing validated records, and controlling access to employee information.

All employee records used in this project are fictional.

## Technologies

- Python 3
- SQLite
- SQL
- Python unittest
- unittest.mock

## Key Features

### 1. Data Quality Analysis
- Identifies missing employee names
- Detects potential duplicate records
- Reports data quality issues

### 2. ETL Pipeline
- Extracts sample employee records
- Removes incomplete and duplicate entries
- Loads validated records into SQLite

### 3. Role-Based Access Control
Implements three roles:

- Admin: Public, Internal, Confidential
- Analyst: Public, Internal
- Viewer: Public

Unknown roles are denied by default.

### 4. Controlled Database Access
- Checks authorization before querying employee records
- Rejects unauthorized requests
- Uses parameterized SQL for employee inserts

### 5. Automated Security Testing
Ten automated tests cover:
- Role permission decisions
- Unauthorized access rejection
- Unknown roles and classifications
- Database access behavior using mocks

### 6. Audit Logging
- Records allowed and denied access attempts
- Logs user roles, requested resources, and access decisions
- Uses Python's built-in logging module
- Stores audit records locally in audit.log
- Includes automated tests for audit logging

## Sample ETL Results

| Metric | Result |
|---|---|
| Original records | 6 |
| Invalid records | 1 |
| Potential duplicates | 1 |
| Clean records loaded | 4 |

## How to Run

Run the ETL pipeline:

```bash
python3 etl_pipeline.py
```

Run the access control demonstration:

```bash
python3 secure_access.py
```

Run the automated tests:

```bash
python3 -m unittest discover -p "test_*.py" -v
```

## Security Scope

This is an educational prototype.

RBAC is enforced within the application's database access function. It does not provide user authentication, database encryption, or protection against direct access to the SQLite file.

The duplicate detection rule is simplified for demonstration purposes.

## Future Improvements

- Data classification metadata
- More comprehensive data validation
- Stronger identity and access management
- Automated reporting and monitoring

## Author

Alanood Abdullah Aldumaiji

Information Systems – Cybersecurity
Prince Sultan University