from mysql.connector import MySQLConnection, Error
from org.anderes.edu.python.python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')
        return conn;
    
    except Error as e:
        print(e)
        raise e
 
    """ finally:
        conn.close()
        print('Connection closed.')
     """
 
if __name__ == '__main__':
    connect()