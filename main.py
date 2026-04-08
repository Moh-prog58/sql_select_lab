import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("----------------Employee Data----------------")
print(employee_data)
print("----------------End Employee Data----------------")

df_first_five = pd.read_sql("""
    SELECT EmployeeID, LastName 
    FROM employees
""", conn)

df_five_reverse = pd.read_sql("""
    SELECT LastName, EmployeeID 
    FROM employees
""", conn)

df_alias = pd.read_sql("""
    SELECT LastName, EmployeeID AS ID 
    FROM employees
""", conn)

df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN JobTitle IN ('President', 'VP Sales', 'VP Marketing') 
            THEN 'Executive' 
            ELSE 'Not Executive' 
        END AS role
    FROM employees
""", conn)

df_name_length = pd.read_sql("""
    SELECT LastName, LENGTH(LastName) AS name_length 
    FROM employees
""", conn)

df_short_title = pd.read_sql("""
    SELECT JobTitle, SUBSTR(JobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)

order_details = pd.read_sql("""SELECT * FROM orderDetails""", conn)
print("----------------Order Details Data----------------")
print(order_details)
print("----------------End Order Details Data----------------")

sum_total_price = pd.read_sql("""
    SELECT 
        OrderID,
        SUM(ROUND(priceEach * quantityOrdered)) AS total_price
    FROM orderDetails
    GROUP BY OrderID
""", conn)

df_day_month_year = pd.read_sql("""
    SELECT 
        OrderDate,
        SUBSTR(OrderDate, 9, 2) AS day,
        SUBSTR(OrderDate, 6, 2) AS month,
        SUBSTR(OrderDate, 1, 4) AS year
    FROM orders
""", conn)

conn.close()
