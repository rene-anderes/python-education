import unittest
from org.anderes.edu.python.python_mysql_dbconfig import read_db_config

class DbConfigTestCase(unittest.TestCase):
    def test_read_config(self):
        db_config = read_db_config()
        print(db_config)
        assert db_config['host'] == "localhost"
        assert db_config['database'] == "mydatabase"
        
        
if __name__ == '__main__':
    unittest.main()