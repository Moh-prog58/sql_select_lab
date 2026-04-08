import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# STEP 1
employee_data = pd.read_sql("""SELECT * FROM Employees""", conn)
print("----------------Employee Data----------------")
print(employee_data)
print("----------------End Employee Data----------------")

# STEP 2
df_first_five = pd.read_sql("""
    SELECT EmployeeID, LastName 
    FROM Employees
""", conn)

# STEP 3
df_five_reverse = pd.read_sql("""
    SELECT LastName, EmployeeID 
    FROM Employees
""", conn)

# STEP 4
df_alias = pd.read_sql("""
    SELECT LastName, EmployeeID AS ID 
    FROM Employees
""", conn)

# STEP 5 - CASE using Title column
df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN Title IN ('President', 'VP Sales', 'VP Marketing') 
            THEN 'Executive' 
            ELSE 'Not Executive' 
        END AS role
    FROM Employees
""", conn)

# STEP 6
df_name_length = pd.read_sql("""
    SELECT LastName, LENGTH(LastName) AS name_length 
    FROM Employees
""", conn)

# STEP 7
df_short_title = pd.read_sql("""
    SELECT Title, SUBSTR(Title, 1, 2) AS short_title 
    FROM Employees
""", conn)

# Order Details reference
order_details = pd.read_sql("""SELECT * FROM "Order Details" """, conn)
print("----------------Order Details Data----------------")
print(order_details.head())
print("----------------End Order Details Data----------------")

# STEP 8 - Using correct column names UnitPrice and Quantity
sum_total_price = pd.read_sql("""
    SELECT 
        OrderID,
        SUM(ROUND(UnitPrice * Quantity)) AS total_price
    FROM "Order Details"
    GROUP BY OrderID
""", conn)

# STEP 9
df_day_month_year = pd.read_sql("""
    SELECT 
        OrderDate,
        SUBSTR(OrderDate, 9, 2) AS day,
        SUBSTR(OrderDate, 6, 2) AS month,
        SUBSTR(OrderDate, 1, 4) AS year
    FROM Orders
""", conn)

conn.close()