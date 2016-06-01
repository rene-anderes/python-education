from mysql.connector import Error
from org.anderes.edu.python.python_mysql_connect import connect


class Employee:
    
    def __init__(self, firstname, lastname, age):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_age(self):
        return self.__age

    def set_firstname(self, value):
        self.__firstname = value

    def set_lastname(self, value):
        self.__lastname = value

    def set_age(self, value):
        self.__age = value
        
    def __repr__(self):
        return str((self.firstname, self.lastname, self.age))
    
    firstname = property(get_firstname, set_firstname, None, None)
    lastname = property(get_lastname, set_lastname, None, None)
    age = property(get_age, set_age, None, None)
    

def getAllEmployees():
    try:
        print("employees")
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT  * FROM employees")
        rows = cursor.fetchall()
        
        employees = [ (Employee(row[3], row[2], row[1])) for row in rows ]
        
        return employees
    
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


