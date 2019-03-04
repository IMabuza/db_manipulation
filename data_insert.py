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
"CREATE TABLE IF NOT EXISTS orders ( ordersID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, customerID INT NOT NULL,orderDate DATETIME, requiredDate DATETIME,shippedDate DATETIME,status VARCHAR(60));"]

sqlStr = ["INSERT INTO customers (firstName, lastName, gender, address, phone, email, city, country) VALUES (%s, %s, %s,%s, %s,%s, %s, %s)",
"INSERT INTO employees (firstName, lastName, email, jobTitle) VALUES (%s, %s, %s,%s)",
"INSERT INTO orders (customerID, orderDate, requiredDate, shippedDate, status) VALUES (%s, %s, %s,%s,%s)"]

val = [[("John","Hibert","Male","284 chaucer st",84789657,
"john@gmail.com","Johannesburg","South Africa"),
("Thando","Sithole","Female","240 Sect 1",794445584,
"thando@gmail.com","Cape Town","South Africa"),
("Leon","Glen","Male","81 Everton Rd,Gillits",820832830,
"Leon@gmail.com","Durban","South Africa"),
("Charl","Muller","Male","290A Dorset Ecke",856872553,
"Charl.muller@yahoo.com","Berlin","Germany"),
("Julia","Stein", "Female","2 Wernerring",672445058,"Js234@yahoo.com",
"Frankfurt","Germany")],

[("Kani","Matthew","Kmat@gmail.com","Manager"),
("Lesly","Cronje","LesC@gmail.com","Clerk"),
("Gideon", "Maduku","Gm@gmail.com","Accountant")],

[(1,'2018-01-09','2018-05-09','2018-02-09',"Not Shipped"),
(3,'2018-01-09','2018-04-09','2018-03-09','Shipped'),
(4,'2018-01-09','2018-03-09','2018-02-09','Not shipped')]


]

for cs in range(len(createStr)):
  
  mycursor.execute(createStr[cs])

  sql = sqlStr[cs]
  
  mycursor.executemany(sql, val[cs])
  
  mydb.commit()
  
  print(mycursor.rowcount, "record(s) inserted.")
