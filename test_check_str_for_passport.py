import unittest
from function_realisation import check_str_for_passport
class MyTestCase(unittest.TestCase):
    def test_valid_passport(self):
        valid_cases = ["1144 099900","0000 000000", "3553 747747"]
        for passport_lines in valid_cases:
            with self.subTest(failed_valid_case=passport_lines):
                self.assertTrue(check_str_for_passport(passport_lines))
    def test_invalid_passport(self):
        invalid_cases = ["","uu","999 000000","4444d667788"," 4444 999999 "]
        for passport_lines in invalid_cases:
            with self.subTest(failed_invalid_case=passport_lines):
                self.assertFalse(check_str_for_passport(passport_lines))

if __name__ == '__main__':
    unittest.main()
