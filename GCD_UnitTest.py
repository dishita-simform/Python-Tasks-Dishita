import unittest

from Dishita_Python_GCD import compute_gcd, gcd, number_to_word, word_to_number

class TestWordNumberGCD(unittest.TestCase):

    def test_word_to_number(self):
        self.assertEqual(word_to_number("one"), 1)
        self.assertEqual(word_to_number("two"), 2)
        self.assertEqual(word_to_number("eight"), 8)
        self.assertEqual(word_to_number("zero"), 0)
        self.assertEqual(word_to_number("minusfive"), None)

    def test_number_to_word(self):
        self.assertEqual(number_to_word(1), "one")
        self.assertEqual(number_to_word(5), "five")
        self.assertEqual(number_to_word(9), "nine")
        self.assertEqual(number_to_word(0), "zero")

    def test_gcd(self):
        self.assertEqual(gcd(8, 12), 4)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(17, 5), 1)
        self.assertEqual(gcd(100, 10), 10)

    def test_compute_gcd(self):
        self.assertIn("GCD in Number: 2", compute_gcd("two", "four"))
        self.assertIn("GCD in Words: one", compute_gcd("three", "five"))
        self.assertEqual(compute_gcd("minusone", "five"), "Invalid Input. Please Enter Valid Positive Word Numbers")
        self.assertEqual(compute_gcd("zero", "five"), "Invalid Input. Please Enter Valid Positive Word Numbers")

if __name__ == "__main__":
    unittest.main()