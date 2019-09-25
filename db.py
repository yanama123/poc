import mysql.connector

try:

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="adminadmin",
    # auth_plugin='mysql_native_password',
    database = 'mydatabase'
  )
  mycursor = mydb.cursor()
  # mycursor.execute("CREATE DATABASE mydatabase")
  mycursor.execute("SHOW DATABASES")
  for x in mycursor:
    print(x)
  # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  mycursor.execute("SHOW TABLES")
  for x in mycursor:
       print(x)
   



except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))