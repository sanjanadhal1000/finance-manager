import os
import unittest
from finance_manager import FinanceManager

class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.fm = FinanceManager(self.test_file)
        self.fm.register_user("testuser", "pass")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_registration(self):
        self.assertTrue(self.fm.register_user("new", "123"))

    def test_duplicate_user_registration(self):
        self.assertFalse(self.fm.register_user("testuser", "xxx"))

    def test_add_income(self):
        self.assertTrue(self.fm.add_transaction("testuser", "income", "Job", 1000, "Salary", "2025-10-30"))

    def test_add_invalid_amount(self):
        self.assertFalse(self.fm.add_transaction("testuser", "income", "Job", -50, "Invalid", "2025-10-30"))

if __name__ == "__main__":
    unittest.main()
