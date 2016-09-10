def cube(x):
    """Given a number, return its cube.""" 
    return x ** 3


import unittest
class MyTest(unittest.TestCase):
    def test_cube(self):
        self.assertEqual( cube(5), 125 )
        self.assertEqual( cube(0), 0 )
        self.assertEqual( cube(1), 1 )

unittest.main()

