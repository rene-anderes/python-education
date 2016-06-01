import unittest
import org.anderes.edu.python.python_mysql_repository as repository
# import org.anderes.edu.python.python_mysql_repository.Employee as employee

class RepositoryTestCase(unittest.TestCase):
    
    def test_result(self):
        employees = repository.getAllEmployees()
        self.assertIsNotNone(employees)
        self.assertEqual(4, len(employees))
        self.__dump(employees)

    def __dump(self, employees):
        for employee in employees:
            print(employee)
        
if __name__ == '__main__':
    unittest.main()