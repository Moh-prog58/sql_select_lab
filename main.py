import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

print("✅ Database Connected Successfully!\n")

print("Employee Table Preview:")
print(pd.read_sql("SELECT EmployeeID, FirstName, LastName, Title FROM Employees LIMIT 5", conn))

df_first_five = pd.read_sql("""
    SELECT EmployeeID, LastName 
    FROM Employees 
    LIMIT 5
""", conn)

df_five_reverse = pd.read_sql("""
    SELECT LastName, EmployeeID 
    FROM Employees 
    LIMIT 5
""", conn)

df_alias = pd.read_sql("""
    SELECT EmployeeID AS 'ID', LastName 
    FROM Employees 
    LIMIT 5
""", conn)
df_executive = pd.read_sql("""
    SELECT 
        EmployeeID,
        FirstName,
        LastName,
        Title,
        CASE 
            WHEN Title IN ('President', 'Vice President, Sales', 'Vice President, Marketing') 
                THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM Employees
""", conn)

df_name_length = pd.read_sql("""
    SELECT 
        LastName,
        LENGTH(LastName) AS name_length
    FROM Employees
""", conn)

df_short_title = pd.read_sql("""
    SELECT 
        SUBSTR(Title, 1, 2) AS short_title
    FROM Employees
""", conn)

sum_total_price_df = pd.read_sql("""
    SELECT ROUND(SUM(UnitPrice * Quantity)) AS total_amount
    FROM "Order Details"
""", conn)
sum_total_price = sum_total_price_df.iloc[0]['total_amount']

df_day_month_year = pd.read_sql("""
    SELECT 
        OrderDate,
        strftime('%d', OrderDate) AS day,
        strftime('%m', OrderDate) AS month,
        strftime('%Y', OrderDate) AS year
    FROM Orders
    LIMIT 10
""", conn)

conn.close()

print("\n=== STEP 2: EmployeeID and LastName (first 5) ===")
print(df_first_five)

print("\n=== STEP 3: LastName before EmployeeID ===")
print(df_five_reverse)

print("\n=== STEP 4: Aliased as 'ID' ===")
print(df_alias)

print("\n=== STEP 5: Executive Role (first 10) ===")
print(df_executive.head(10))

print("\n=== STEP 6: Last Name Length (first 5) ===")
print(df_name_length.head())

print("\n=== STEP 7: Short Title (first 5) ===")
print(df_short_title.head())

print(f"\n=== STEP 8: Total Order Amount ===\n{sum_total_price}")

print("\n=== STEP 9: Order Date as Day/Month/Year ===")
print(df_day_month_year)

print("\n🎉 All steps completed successfully!")