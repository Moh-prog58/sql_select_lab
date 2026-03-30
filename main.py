cat > main.py << 'EOF'
import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

print("Connected to database\n")

tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Available tables:")
print(tables)

try:
    preview = pd.read_sql("SELECT EmployeeID, FirstName, LastName, Title FROM Employees LIMIT 5", conn)
    table_name = "Employees"
    print(f"\nUsing table: {table_name}")
except:
    try:
        preview = pd.read_sql("SELECT EmployeeID, FirstName, LastName, Title FROM employees LIMIT 5", conn)
        table_name = "employees"
        print(f"\nUsing table: {table_name}")
    except Exception as e:
        print("Error reading employees table:", e)
        table_name = None

if table_name is None:
    print("Could not find employees table. Check table names above.")
    conn.close()
else:
    print("\nEmployee Preview:")
    print(preview)

    df_first_five = pd.read_sql(f"SELECT EmployeeID, LastName FROM {table_name} LIMIT 5", conn)

    df_five_reverse = pd.read_sql(f"SELECT LastName, EmployeeID FROM {table_name} LIMIT 5", conn)

    df_alias = pd.read_sql(f"SELECT EmployeeID AS 'ID', LastName FROM {table_name} LIMIT 5", conn)

    df_executive = pd.read_sql(f"""
        SELECT EmployeeID, FirstName, LastName, Title,
               CASE WHEN Title IN ('President', 'Vice President, Sales', 'Vice President, Marketing') 
                    THEN 'Executive' ELSE 'Not Executive' END AS role
        FROM {table_name}
    """, conn)

    df_name_length = pd.read_sql(f"SELECT LastName, LENGTH(LastName) AS name_length FROM {table_name}", conn)

    df_short_title = pd.read_sql(f"SELECT SUBSTR(Title, 1, 2) AS short_title FROM {table_name}", conn)

    sum_total_price_df = pd.read_sql('SELECT ROUND(SUM(UnitPrice * Quantity)) AS total_amount FROM "Order Details"', conn)
    sum_total_price = sum_total_price_df.iloc[0]['total_amount']

    df_day_month_year = pd.read_sql("""
        SELECT OrderDate, 
               strftime('%d', OrderDate) AS day,
               strftime('%m', OrderDate) AS month,
               strftime('%Y', OrderDate) AS year
        FROM Orders LIMIT 10
    """, conn)

    conn.close()

    print("\n=== STEP 2 ===")
    print(df_first_five)

    print("\n=== STEP 3 ===")
    print(df_five_reverse)

    print("\n=== STEP 4 ===")
    print(df_alias)

    print("\n=== STEP 5 (head) ===")
    print(df_executive.head())

    print("\n=== STEP 6 (head) ===")
    print(df_name_length.head())

    print("\n=== STEP 7 (head) ===")
    print(df_short_title.head())

    print(f"\n=== STEP 8 Total Amount ===\n{sum_total_price}")

    print("\n=== STEP 9 (head) ===")
    print(df_day_month_year.head())

    print("\n🎉 All steps completed!")
EOF