import unittest

from Dishita_Python_Parenthesis import generate_parentheses

class TestGenerateParentheses(unittest.TestCase):

    def test_generate_parentheses(self):
        self.assertEqual(generate_parentheses(1), ["()"])
        self.assertEqual(generate_parentheses(2), ["(())", "()()"])
        self.assertEqual(generate_parentheses(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(len(generate_parentheses(4)), 14)  # There are 14 valid combinations for n=4
        self.assertEqual(len(generate_parentheses(5)), 42)  # There are 42 valid combinations for n=5

    def test_invalid_input(self):
        self.assertEqual(generate_parentheses(0), [])  # Edge case: No parentheses for n=0
        self.assertEqual(generate_parentheses(-1), [])  # Edge case: Negative input should return an empty list

if __name__ == "__main__":
    unittest.main()
