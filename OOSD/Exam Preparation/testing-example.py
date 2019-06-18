import unittest


class Square():

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class SquareTest(unittest.TestCase):
    def setUp(self):
        self.s = Square(6)

    def test_area(self):
        result = self.s.area()
        self.assertEqual(result, 36)

    def test_perimeter(self):
        result = self.s.perimeter()
        self.assertEqual(result, 24)

    def tearDown(self):
        self.s = None


if __name__ == '__main__':
    unittest.main()
