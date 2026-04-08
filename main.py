import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM Employees""", conn)
print("----------------Employee Data----------------")
print(employee_data)
print("----------------End Employee Data----------------")

df_first_five = pd.read_sql("""
    SELECT EmployeeID, LastName 
    FROM Employees
    ORDER BY EmployeeID
""", conn)

df_five_reverse = pd.read_sql("""
    SELECT LastName, EmployeeID 
    FROM Employees
    ORDER BY EmployeeID
""", conn)

df_alias = pd.read_sql("""
    SELECT LastName, EmployeeID AS ID 
    FROM Employees
    ORDER BY EmployeeID
""", conn)

df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN Title IN ('President', 'Vice President, Sales', 'VP Sales', 
                          'VP Marketing', 'Sales Manager') 
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

df_short_title = pd.read_sql("""
    SELECT Title, SUBSTR(Title, 1, 2) AS short_title 
    FROM Employees
    ORDER BY EmployeeID
""", conn)

order_details = pd.read_sql("""SELECT * FROM "Order Details" """, conn)
print("----------------Order Details Data----------------")
print(order_details.head())
print("----------------End Order Details Data----------------")

total_df = pd.read_sql("""
    SELECT SUM(ROUND(UnitPrice * Quantity)) AS total_price
    FROM "Order Details"
""", conn)
sum_total_price = total_df.iloc[0, 0]   

df_day_month_year = pd.read_sql("""
    SELECT 
        OrderDate,
        SUBSTR(OrderDate, 4, 2) AS day,      -- day for MM/DD/YYYY
        SUBSTR(OrderDate, 1, 2) AS month,    -- month
        SUBSTR(OrderDate, 7, 4) AS year      -- year
    FROM Orders
    ORDER BY OrderID
    LIMIT 10
""", conn)

conn.close()