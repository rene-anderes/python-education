import mysql.connector
from mysql.connector import Error
from org.anderes.edu.python.python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    
    try:
        print('Connecting to MySQL database...')
        conn = mysql.connector.connect(pool_name = "mypool", pool_size = 3, **db_config)
 
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')
        return conn;
    
    except Error as e:
        print(e)
        raise e
 
if __name__ == '__main__':
    connect()