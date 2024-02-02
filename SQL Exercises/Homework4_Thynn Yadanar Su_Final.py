import pandas as pd
import sqlite3 

#create database
dbpath = 'DataSource\MyCompany.db'
conn = sqlite3.connect(dbpath, timeout=10)
cur = conn.cursor()

def display_data(myvalue):
    for row in myvalue:
        print("EMPLOYEE ID:",row[0])
        print("FIRST_NAME: ",row[1])
        print("LAST_NAME:  ",row[2])
        print("EMAIL:      ",row[3])
        print("PHONE_NUMBER:",row[4])
        print("HIRE_DATE:   ",row[5])
        print("JOB_ID:      ",row[6])
        print("SALARY:      ",row[7])
        print("MANAGER_ID:  ",row[8])
        print("DEPARTMENT_ID:",row[9])
        print("*********")

print("\n------------ Created table successfully----------------")

# conn.execute('''
#               CREATE TABLE MyEmployees
#               (
#                   EMPLOYEE_ID   INT PRIMARY KEY,
#                   FIRST_NAME    CHAR(20) NOT NULL,
#                   LAST_NAME     CHAR(20) NOT NULL,
#                   EMAIL         CHAR(20) NOT NULL,
#                   PHONE_NUMBER  CHAR(20) NOT NULL,
#                   HIRE_DATE     CHAR(20) NOT NULL,
#                   JOB_ID        CHAR(20) NOT NULL,
#                   SALARY        REAL NOT NULL,
#                   MANAGER_ID	  INT, 
#                   DEPARTMENT_ID INT NOT NULL
#                   );
#             ''' )
                
# ----------------------------------------------------------------------------
#read the data from the  csv file
df_csv = pd.read_csv(r'DataSource/employees.csv')

#changing the retrieved data into a sql format
records_csv = df_csv.to_sql('MyEmployees', conn, if_exists = 'replace', index=False)
conn.commit()

print("\n---------------------------------------------------\n")
print("--- Data from the CSV file are inserted into the table successfully ---")

# ----------------------------------------------------------------------------
#read the data from the json file
df_json = pd.read_json(r'DataSource/employees.json')

#changing the retrieved data into a sql format
records_json = df_json.to_sql('MyEmployees', conn, if_exists = 'append', index=False)
conn.commit()

print("\n----------------------------------------------------\n")
print("--- Data from the JSON file are inserted into the table successfully ---\n")

#-----------------------------------------------------------------------------
#select
print("\n----------- Employees whose salary is above 7000 ---------\n")
emp_salary = cur.execute('SELECT * FROM MyEmployees WHERE SALARY>7000')
display_data(emp_salary)

#-----------------------------------------------------------------------------
#update
# print("\n----------- The employee's salary whose ID is 112 is set to 7900  ---------\n")
# conn.execute('UPDATE MyEmployees SET SALARY=7900 WHERE EMPLOYEE_ID=112')
# emp_select1 = cur.execute("SELECT * FROM MyEmployees")
# display_data(emp_select1)

#-----------------------------------------------------------------------------
#delete

# conn.execute('''
#               DELETE FROM 'MyEmployees' WHERE LAST_NAME = 'Fay';
#               ''')
# emp_select2 = cur.execute("SELECT * FROM MyEmployees")
# display_data(emp_select2)
# print("\n----------- Employees with the last name, Fay are already deleted  ---------\n")
conn.close()