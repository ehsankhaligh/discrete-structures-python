def shifter (n, k):

    return ( n + k ) % 128

def shiftcipher(bstr, k):

    return bytes( [ shifter(n, k) for n in bstr ] )


import unittest
                  
class MyTest(unittest.TestCase):

    def test_shifter(self):
        self.assertEqual( shifter(43, 100), 15 )
        self.assertEqual( shifter(97, 54), 23 )
        self.assertEqual( shifter(112, 86), 70 )
    def test_shiftcipher(self):
        self.assertEqual( shiftcipher(b'hello', 15) )
        self.assertEqual( shiftcipher(b'Sierra', 105) )
        self.assertEqual( shiftcipher(b'Discrete Structures', 117) )
        
unittest.main()
