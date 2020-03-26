import pyodbc

server ='localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()
#
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# print("The row is", row)

# cust_rows = cursor.execute("SELECT * FROM Customers;").fetchone()
# print("The row is", cust_rows)

# rows = cursor.execute("SELECT*FROM Products").fetchall()
# print("Unit price")
# for record in rows:
#     print(record.UnitPrice)

##List lastname of employees

# last_name = cursor.execute("SELECT lastname FROM Employees")
# print("Last Name")
#
# for list in last_name:
#     print(list.lastname)

#List employees in Seattle and London

# employees = cursor.execute("SELECT * FROM Employees WHERE City IN ('London','Seattle');").fetchall()
# print("Employees living in London and Seattle:")
# for list in employees:
#     print(list.FirstName, list.LastName)