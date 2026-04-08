import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# Drop any old view
conn.execute("DROP VIEW IF EXISTS employees;")

# Create view with exactly what the test expects: table 'employees' and column 'employeeID'
conn.execute("""
    CREATE VIEW employees AS
    SELECT 
        EmployeeID AS employeeID,
        LastName,
        FirstName,
        Title
    FROM Employees;
""")

print("✅ View 'employees' created successfully!")

# Verify
print("\nColumns in the new 'employees' view:")
print(pd.read_sql("PRAGMA table_info(employees);", conn))

conn.close()
