import unittest

from Dishita_Python_Parenthesis import generate_parentheses

class TestGenerateParentheses(unittest.TestCase):

    def test_generate_parentheses(self):
        self.assertEqual(generate_parentheses(1), ["()"])
        self.assertEqual(generate_parentheses(2), ["(())", "()()"])
        self.assertEqual(generate_parentheses(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(len(generate_parentheses(4)), 14) 
        self.assertEqual(len(generate_parentheses(5)), 42)  

    def test_invalid_input(self):
        self.assertEqual(generate_parentheses(0), [])  
        self.assertEqual(generate_parentheses(-1), [])  

if __name__ == "__main__":
    unittest.main()
