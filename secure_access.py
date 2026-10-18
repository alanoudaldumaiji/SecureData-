import sqlite3

from pathlib import Path

from security import check_access

from audit_logger import log_access



DB_PATH = Path(__file__).parent / "securedata.db"





def get_employees(role):

    classification = "Internal"



    if not check_access(role, classification):
        log_access(role, "Employee Directory", False)

        raise PermissionError(

            f"Access denied: {role} cannot read Internal data"

        )


    log_access(role, "Employee Directory", True)
    
    connection = sqlite3.connect(DB_PATH)



    try:

        cursor = connection.cursor()

        cursor.execute("""

            SELECT id, name, department

            FROM clean_employees

        """)

        results = cursor.fetchall()

        return results



    finally:

        connection.close()





if __name__ == "__main__":

    for role in ["Admin", "Analyst", "Viewer", "Unknown"]:

        print(f"\nRole: {role}")



        try:

            employees = get_employees(role)

            print("ACCESS GRANTED")

            print("Records returned:", len(employees))



        except PermissionError as error:

            print(error)