import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="umuzi"
)

mycursor = mydb.cursor()

#Create list of "Create" statement strings

createStr = ["CREATE TABLE IF NOT EXISTS customers(customerID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(30) NOT NULL, lastName VARCHAR(30) NOT NULL, gender ENUM('Male', 'Female') NOT NULL, address VARCHAR(60) NOT NULL, phone INT(15) NOT NULL, email VARCHAR(30) NOT NULL, city VARCHAR(60) NOT NULL, country VARCHAR(60) NOT NULL);",
"CREATE TABLE IF NOT EXISTS employees(EmployeeID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,firstName VARCHAR(30) NOT NULL, lastName VARCHAR(30) NOT NULL, email VARCHAR(60) NOT NULL, jobTitle VARCHAR(30) NOT NULL);",
"CREATE TABLE IF NOT EXISTS orders ( ordersID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,orderDate DATETIME, requiredDate DATETIME,shippedDate DATETIME,status VARCHAR(60));",
"CREATE TABLE IF NOT EXISTS payments( CustomerID INT  UNSIGNED,paymentDate DATETIME, amount DECIMAL,FOREIGN KEY(CustomerID) REFERENCES customers(customerID) ON DELETE CASCADE);",
"CREATE TABLE IF NOT EXISTS products(productId INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, productName VARCHAR(100) NOT NULL, description VARCHAR(200) NOT NULL, buyPrice DECIMAL);" 
]

sqlStr = ["INSERT INTO customers (firstName, lastName, gender, address, phone, email, city, country) VALUES (%s, %s, %s,%s, %s,%s, %s, %s)",
"INSERT INTO employees (firstName, lastName, email, jobTitle) VALUES (%s, %s, %s,%s)",
"INSERT INTO orders (orderDate, requiredDate, shippedDate, status) VALUES (%s, %s, %s,%s)",
"INSERT INTO payments (customerID, paymentDate, amount) VALUES (%s, %s, %s)",
"INSERT INTO products (productName, description, buyPrice) VALUES (%s, %s, %s)"]

val = [[("John","Hibert","Male","284 chaucer st",84789657,
"john@gmail.com","Johannesburg","South Africa"),
("Thando","Sithole","Female","240 Sect 1",794445584,
"thando@gmail.com","Cape Town","South Africa"),
("Leon","Glen","Male","81 Everton Rd,Gillits",820832830,
"Leon@gmail.com","Durban","South Africa"),
("Charl","Muller","Male","290A Dorset Ecke",856872553,
"Charl.muller@yahoo.com","Berlin","Germany"),
("Julia","Stein", "Female","2 Wernerring",672445058,"Js234@yahoo.com",
"Frankfurt","Germany"),],

[("Kani","Matthew","Kmat@gmail.com","Manager"),
("Lesly","Cronje","LesC@gmail.com","Clerk"),
("Gideon", "Maduku","Gm@gmail.com","Accountant")],

[('2018-01-09','2018-05-09','2018-02-09',"Not Shipped"),
('2018-01-09','2018-04-09','2018-03-09','Shipped'),
('2018-01-09','2018-03-09','2018-02-09','Not shipped')],

[(1,'2018-01-09',100.00),(2, '2018-01-09',250.75)],

[("Harley Davidson Chopper", "This replica features working kickstand, front suspension, gear-shift lever", 150.75),
("Classic Car","Turnable front wheels, steering function",550.75),
("Sports car","Turnable front wheels, steering function",700.60)]

]

for cs in range(len(createStr)):
  
  mycursor.execute(createStr[cs])

  sql = sqlStr[cs]
  
  mycursor.executemany(sql, val[cs])
  
  mydb.commit()
  
  print(mycursor.rowcount, "record(s) inserted.")

def iter_results():

  result = mycursor.fetchall()
  for r in result:
    print(r)

  print("#####################################################")
  print(" ")
  print("#####################################################")


# SELECT ALL records from table Customers
mycursor.execute("SELECT * FROM customers;")

print("ALL records from table Customers")

iter_results()

# SELECT records only from the name column in the Customers table

mycursor.execute("SELECT firstName FROM customers;")

print("records only from the name column in the Customers table")

iter_results()

#Show the name of the Customer whose CustomerID is 1
mycursor.execute("SELECT firstName from customers WHERE customerID = 1;")
print("Show the name of the Customer whose CustomerID is 1")
iter_results()

#UPDATE the record for CustomerID =1  on the Customer table so that the name is “Lerato Mabitso”.

mycursor.execute("UPDATE customers SET firstName = 'Lerato', lastName = 'Mabitso' WHERE customerID = 1;")

print("UPDATE the record for CustomerID = 1  on the Customer table so that the name is Lerato Mabitso")

mycursor.execute("SELECT firstName from customers WHERE customerID = 1;")

iter_results()

#DELETE the record from the Customers table for customer 2 (CustomerID = 2).

mycursor.execute("DELETE FROM customers WHERE customerID = 2;")

print("customerID 2 Deleted")


#Select all unique values from the table Products.

mycursor.execute("SELECT DISTINCT productName FROM products;")

print("Select all unique values from the table Products.")

iter_results()

#Return the MAXIMUM payment made on the PAYMENTS table
mycursor.execute("SELECT MAX(amount) FROM payments;")

print("Return the MAXIMUM payment made on the PAYMENTS table")

iter_results()


#Create a query that selects all customers from the "Customers" table, sorted by the "Country" column.
mycursor.execute("SELECT * FROM customers ORDER BY country ASC;")

print("Create a query that selects all customers from the Customers table, sorted by the Country column.")

iter_results()

#Create a query that selects all Products with a price BETWEEN R100 and R600.

mycursor.execute("SELECT * FROM products WHERE buyPrice > 100 and buyPrice < 600;")

print("Create a query that selects all Products with a price BETWEEN R100 and R600.")

iter_results()

#Create a query that selects all fields from "Customers" where country is "Germany" AND city is "Berlin".

mycursor.execute("SELECT * FROM customers WHERE country = 'germany' and city = 'berlin';")

print("Create a query that selects all fields from Customers where country is Germany AND city is Berlin.")

iter_results()

#Create a query that selects all fields from "Customers" where city is "Cape Town" OR "Durban".

mycursor.execute("SELECT * FROM customers WHERE city = 'germany' OR city = 'berlin';")

print("Create a query that selects all fields from Customers where city is Cape Town OR Durban")

iter_results()


#Select all records from Products where the Price is GREATER than R500.

mycursor.execute("SELECT * FROM products WHERE buyPrice > 500;")

print("Select all records from Products where the Price is GREATER than R500.")

iter_results()

#Return the sum of the Amounts on the Payments table.

mycursor.execute("SELECT SUM(amount) FROM payments;")

print("Return the sum of the Amounts on the Payments table.")

iter_results()

#Count the number of shipped orders in the Orders table.

mycursor.execute("SELECT COUNT(status) FROM orders WHERE status = 'shipped';")

print("Count the number of shipped orders in the Orders table.")

iter_results()

#Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).

mycursor.execute("SELECT COUNT(status) FROM orders WHERE status = 'shipped';")

print("Count the number of shipped orders in the Orders table.")

iter_results()

#Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).

mycursor.execute("SELECT AVG(buyPrice) FROM products;")

print("Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).")

iter_results()













