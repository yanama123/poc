import unittest
import time


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    def testadd1(self):
        print('testadd')
        time.sleep(10)
        self.assertEqual(add(4, 5), 9)


if __name__ == '__main__':
    unittest.main()
