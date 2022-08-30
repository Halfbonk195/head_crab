import unittest
from employee_class import Employee


class EmployeeCaseTest(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('Tim', 'Antipin', 100000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 105000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 110000)


if __name__ == '__main__':
    unittest.main()
