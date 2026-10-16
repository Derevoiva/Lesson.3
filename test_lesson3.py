import unittest
import lesson3 as m

class LessonTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(m.divide(8,2),4)
        self.assertEqual(m.largest_two_sum(1,3,2),5)
        self.assertEqual(m.negative_power(2,-3),0.125)
        self.assertEqual(m.running_sum(["1 2","3 q 999"]),6)
        self.assertEqual(m.capitalize_words("hello world"),"Hello World")

if __name__ == "__main__":
    unittest.main()
