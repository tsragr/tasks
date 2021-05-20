import unittest
import conversion


class TestCalc(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(conversion.celsius_to_fahrenheit(25), 77)
        self.assertEqual(conversion.celsius_to_fahrenheit(30), 86)
        self.assertEqual(conversion.celsius_to_fahrenheit(180), 356)

    def test_meters_to_feet(self):
        self.assertEqual(conversion.meters_to_feet(10), 32.81)
        self.assertEqual(conversion.meters_to_feet(32), 104.99)
        self.assertEqual(conversion.meters_to_feet(50), 164.04)

    def test_ounces_to_grams(self):
        self.assertEqual(conversion.ounces_to_grams(19), 538.64)
        self.assertEqual(conversion.ounces_to_grams(36), 1020.58)
        self.assertEqual(conversion.ounces_to_grams(59), 1672.62)


if __name__ == '__main__':
    unittest.main()
