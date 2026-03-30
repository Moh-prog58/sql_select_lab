import sqlite3

conn = sqlite3.connect('data.sqlite')

conn.execute("DROP VIEW IF EXISTS employees;")

conn.execute("""
    CREATE VIEW employees AS 
    SELECT 
        EmployeeID AS employeeID,
        LastName,
        FirstName,
        Title
    FROM Employees;
""")

print("✅ Created view 'employees' with employeeID column")

print("\nColumns in the new view:")
print(pd.read_sql("PRAGMA table_info(employees);", conn))

conn.close()
print("\nView created successfully. Now run pytest.")
