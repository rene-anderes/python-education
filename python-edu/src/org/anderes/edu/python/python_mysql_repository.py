from mysql.connector import Error
from org.anderes.edu.python.python_mysql_connect import connect


class Employee:
    
    def __init__(self, firstname, lastname, age, db_id):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__id = db_id

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_age(self):
        return self.__age
    
    def get_id(self):
        return self.__id

    def set_firstname(self, value):
        self.__firstname = value

    def set_lastname(self, value):
        self.__lastname = value

    def set_age(self, value):
        self.__age = value
        
    def __repr__(self):
        return str((self.firstname, self.lastname, self.age, self.id))
    
    firstname = property(get_firstname, set_firstname, None, None)
    lastname = property(get_lastname, set_lastname, None, None)
    age = property(get_age, set_age, None, None)
    id = property(get_id, None, None, None)

def getAllEmployees():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        
        employees = [ (Employee(row[3], row[2], row[1], row[0])) for row in rows ]
        
        return employees
    
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


