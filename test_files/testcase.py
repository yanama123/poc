import unittest
import time


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    def test_add1(self):
        print('testadd')
        time.sleep(10)
        self.assertEqual(add(4, 5), 9)
    def test_add2(self):
        print('testadd')
        time.sleep(10)
        self.assertEqual(add(2, 3), 5)
    def test_add3(self):
        print('testadd')
        time.sleep(10)
        self.assertNotEqual(add(2, 4), 7)


if __name__ == '__main__':
    unittest.main()
