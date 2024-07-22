# Final Project IT412
# Testing Program

import unittest
from functions.functions import * 

### To do list:
# Verify how the unitest module is supposed to run and from what folder 

class ValidNames(unittest.TestCase):
    """Tests for functions in the functions.py file"""

    def test_sql_fix(self):
        """Test method used to test single quote inputs for SQL queries"""
        test = "persh'"
        self.assertEqual(test + "\'",fixForSQL(test))

    def test_valid_address(self):
        """Test method used to test valid and invalid address inputs"""
        valid_inputs = ["1234 Main St", "134", "Street"]
        invalid_inputs = ["123@ Main", "", "*&"]

        for input in valid_inputs:
            self.assertTrue(is_valid_address(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_address(input))

    def test_valid_city(self):
        """Test method used to test valid and invalid city inputs"""
        valid_inputs = ["'", "City", "Kansas City", "O'Fallon", "'Pittsburgh"]
        invalid_inputs = ["123 City", "#", "", "\""]

        for input in valid_inputs:
            self.assertTrue(is_valid_city(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_city(input))
       
    def test_valid_email(self):
        """Test method used to test valid and invalid email inputs"""
        valid_inputs = [".", "@", "trevor@email.com", "134", "", "tjhg @com"]
        invalid_inputs = ["tjh{@email", "$!*"]

        for input in valid_inputs:
            self.assertTrue(is_valid_email(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_email(input))

    def test_valid_name(self):
        """Test method used to test valid and invalid inputs for names"""
        valid_inputs = ["Trev", "trev", " Trev", "Trev ", " trev", "trev "]
        invalid_inputs = ["Trev#", "Trev134", "Trev&", "Trev+", " T_Trev"]

        for input in valid_inputs:
            self.assertTrue(is_valid_name(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_name(input))

    def test_valid_phone(self):
        """Test method used to test valid and invalid phone number inputs"""
        valid_inputs = ["123-245-1234", "12134-1431245", "2"]
        invalid_inputs = ["1223fghe", "123$51", "3575 35753"]

        for input in valid_inputs:
            self.assertTrue(is_valid_phone(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_phone(input))
       
    def test_valid_state(self):
        """Test method used to test valid and invalid state inputs"""
        valid_inputs = ["MI", "CA", "ZZ"]
        invalid_inputs = ["Dh", "dd", "E3", " ", "$", "dD"]

        for input in valid_inputs:
            self.assertTrue(is_valid_state(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_state(input))

    def test_valid_zip(self):
        """Test method used to test valid and invalid ZIP inputs"""
        valid_inputs = ["4213", "21344"]
        invalid_inputs = ["1", "23", "456282", "jfhw", " "]

        for input in valid_inputs:
            self.assertTrue(is_valid_zip(input))

        for input in invalid_inputs:
            self.assertFalse(is_valid_zip(input))