import unittest
from org.anderes.edu.python.python_mysql_connect import connect

class DbConnectTestCase(unittest.TestCase):
    def test_conect(self):
        conn = connect()
        self.assertIsNotNone(conn, 'Connection ist NONE')
        self.assertTrue(conn.is_connected(), 'Keine Verbindung zum DB-Server')
        conn.close()   
        
if __name__ == '__main__':
    unittest.main()