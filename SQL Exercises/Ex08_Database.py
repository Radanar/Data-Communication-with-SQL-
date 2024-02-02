"""
Created on Sat Sep 22 18:49:52 2023

@author: ACER

Create a database, Create a table in the database, 
Insert, Select, Update, Delete
"""
import pandas as pd
import sqlite3 

def display_data(myvalue):
    for row in myvalue:
        print("The id is",row[0])
        print("The name is",row[1])
        print("The age is",row[2])
        print("The address is",row[3])
        print("The salary is",row[4])
        print("*********")

dbpath = 'DataSource\mycompany.db'
conn = sqlite3.connect(dbpath, timeout=10) #???timeout means the database will be closed after 10 Milli s of the code execution.

print("---Create table---")

# conn.execute('''
#               CREATE TABLE COMPANY
#               (
#                   ID      INT PRIMARY KEY NOT NULL,
#                   NAME    CHAR(20) NOT NULL,
#                   AGE     INT NOT NULL,
#                   ADDRESS CHAR(50),
#                   SALARY  REAL
#                   );   
#               '''  )

print("---Table Created Successfully---")

print("---Insert data---")

conn.execute('''
              INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)
              VALUES (70, "May", 22, "Yangon", 52000)            
              ''')
conn.execute('''
              INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)
              VALUES (40, "Sue", 30, "Vienna", 60000)            
              ''')
conn.execute('''
             INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)
             VALUES (05, "Lily", 20, "Michigan", 75000)            
             ''')
conn.execute('INSERT INTO COMPANY values (?, ?, ?, ?, ?)',  
             (7, "Bond", 25, "Redford", 65000))

data = [
        (11, "Bob", 21, "Ohio", 80000),
        (12, "Daisy", 23, "Taxas", 45000),
        (13, "Dawi", 24, "Denver", 67000)
       ]

conn.executemany('INSERT INTO COMPANY values  (?, ?, ?, ?, ?)', data)

print("---Display before update---")

cur = conn.cursor() #cursor() will retrieve every data from the table by looping - no matter the quantity
result1 = cur.execute("select * from company") #curr.execute retrieved everything from the table Company

#result1 = cur.execute("select * from company where age<25")

display_data(result1)

print("---Display after update---")

conn.execute('''
             UPDATE COMPANY
             SET AGE=10 
             WHERE id = 7
             ''')
conn.execute('''
             UPDATE COMPANY
             SET SALARY = SALARY+SALARY*0.1
             WHERE id = 40
             ''')
result2 = cur.execute("select * from company")
display_data(result2)

print("---Display after the delete---")

conn.execute('''
             DELETE from company where ID=05
            ''')
result3 = cur.execute("select * from company")
display_data(result3)

conn.close()



