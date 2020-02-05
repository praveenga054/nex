#test_employee

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee('Praveen', 'Appinbail', 50000)
        self.emp_2 = Employee('Pooja', 'Appinbail', 60000)


    def tearDown(self):
        pass




    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Praveen.Appinbail@email.com')
        self.assertEqual(self.emp_2.email, 'Pooja.Appinbail@email.com')

        self.emp_1.first = 'Ashwini'
        self.emp_2.first = 'Preetam'

        self.assertEqual(self.emp_1.email, 'Ashwini.Appinbail@email.com')
        self.assertEqual(self.emp_2.email, 'Preetam.Appinbail@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Praveen Appinbail')
        self.assertEqual(self.emp_2.fullname, 'Pooja Appinbail')

        self.emp_1.first = 'Ashwini'
        self.emp_2.first = 'Preetam'

        self.assertEqual(self.emp_1.fullname, 'Ashwini Appinbail')
        self.assertEqual(self.emp_2.fullname, 'Preetam Appinbail')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
