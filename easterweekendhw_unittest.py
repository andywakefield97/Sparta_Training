#Using functions created in "easterweekendhw". We have imported and tested these functions using unit testing.

from easterweekendhw import Apple
import unittest

class Appletests(unittest.TestCase):
    test_apple = Apple("Cox", 600, 4)

    def test_weight_category(self):
        self.assertEqual(self.test_apple.weight_category(),"Large")

    def test_age_category(self):
        self.assertEqual(self.test_apple.age_category(),"Class 1")


if __name__ == '__main__':
    unittest.main()