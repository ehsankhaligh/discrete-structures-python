def linear(m,a,k):

    return (m * a + k )% 256

def linearcipher(bstr ,m,k):

   return bytes( [ linear(m,a,k) for (m*a) in bstr ] ) 
   


import unittest
class MyTest(unittest.TestCase):

    def test_linear(self):
        self.assertEqual( linear(0, 0, 0), 0 ) 
        self.assertEqual( linear(1,4,5), 9 )  
        self.assertEqual( linear(90,8,4), 212 ) 
    def test_linearcipher(self):
        self.assertEqual( linearcipher(b'Sierra', 11, 83) )
        self.assertEqual( linearcipher(b'Discrete Structures', 11, 83) )
        self.assertEqual( linearcipher(b'Hello', 11, 83) )
         
unittest.main()
