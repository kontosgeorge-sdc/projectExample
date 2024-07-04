'''
pip list                                  <- to see the installed libraries
pip install mysql-connector-python
see:
https://www.w3schools.com/python/python_mysql_getstarted.asp
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

if you name your file mysql.py or select.py this is not going to work 
as there are already files with these names imported and the interpreter gets confused
'''

'''
   connect
   select 
   function selectDump(con) - selects and dumps the result
   iterate through, display
   insert
'''

'''
   Here's a bunch of commands you can use in the MySQL workbench side
   USE world;
   SHOW tables;
   DESCRIBE city;
   SELECT * FROM city ORDER BY ID DESC LIMIT 2;
   INSERT INTO city (Name, District, CountryCode) values ("GeorgeCity", "GeorgeDistrict", "PSE");
   DELETE FROM city WHERE Name="GeorgeCity";
'''

import mysql.connector

# settup - database connections 
credentials = mysql.connector.connect(
  host="localhost",
  user="root",
  password="v9bBF(n7fovk",
  database="testdblloyds2"
)


def selectStudents():
  sql = "SELECT * FROM Students;"
  query = credentials.cursor()
  query.execute(sql)
  result = query.fetchall()
  print(result)
  for item in result:
     print(item)

def insertToStudent(fullname, phonenumber, address):
  sql = 'INSERT INTO Students (FullName, PhoneNumber, Address) values (%s, %s, %s);'
  val = [fullname, phonenumber, address]
  # cursor is our way of requesting things from mySQL in Python
  # the query will use the credentials to request info
  query = credentials.cursor()
  query.execute(sql, val)
  credentials.commit()
  print(query.rowcount, "record inserted.")

# ID is the name of the city to be deleted
def deleteStudentsByID(ID):
    sql = "DELETE FROM Students WHERE ID = '%s'" % ID
    query = credentials.cursor()
    query.execute(sql)  
    credentials.commit() # commit the CHANGE in the database  
    latestRow = query.rowcount
    print(latestRow, " record deleted")

# deleteStudentsByID(1)
# insertToStudent("Nero","0123456789","Via Roma 2")
# selectStudents()