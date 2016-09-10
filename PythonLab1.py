#Ehsan Hosseinzadeh Khaligh

def distance(x, y):

    return ( ( x**2 + y**2) ** 0.5 )

def evenodd(n):
    
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

def evenodd_list(lst):

    return [evenodd(i)  for i in lst]


def shifter(n,k):

    return (n + k) % 128
    
def shiftcipher(bstr, k):

    return bytes( [ shifter(b, k) for b in bstr ] )
def linear(m, a, k):
    
    return (m * a + k) % 256

def linearcipher (bstr, m, k):

    return bytes ( [linear(b, m, k) for b in bstr ])

import unittest

class MyTest(unittest.TestCase):
    def test_distance(self):
        self.assertEqual( distance(3, 4), 5 )
        self.assertEqual( distance(0, 0), 0 )
        self.assertEqual( distance(4, 5), 6.4031242374328485 )
        

    def test_evenodd(self):
        self.assertEqual( evenodd(5), 'odd' )
        self.assertEqual( evenodd(6), 'even' )
        self.assertEqual( evenodd(7), 'odd' )

    def test_evenodd_list(self):
        self.assertEqual( evenodd_list( [7, -4] ),  ['odd', 'even'])
        self.assertEqual( evenodd_list( [5, -2] ),  ['odd', 'even'])
        self.assertEqual( evenodd_list( [1, -6] ),  ['odd', 'even'])

    def test_shifter(self):
        self.assertEqual( shifter(43, 100), 15 )
        self.assertEqual( shifter(97, 54), 23 )
        self.assertEqual( shifter(112, 86), 70 )
       
    def test_shiftcipher(self):
        self.assertEqual(shiftcipher(b'hello', 15) , b'wt{{~')
        self.assertEqual(shiftcipher(b'Sierra', 105), b'<RN[[J')
        self.assertEqual(shiftcipher(b'Discrete Structures', 117), b'9^hXgZiZ\x15HigjXijgZh')

    def test_linear(self):
        self.assertEqual( linear(0, 0, 0), 0 ) 
        self.assertEqual( linear(1,4,5), 9 )  
        self.assertEqual( linear(90,8,4), 212 )
        
    def test_linearcipher(self):
        self.assertEqual(linearcipher(b'Sierra', 11, 83), b'\xe4\xd6\xaa99~')
        self.assertEqual(linearcipher(b'Discrete Structures', 11, 83), b'?\xd6D\x949\xaaO\xaa\xb3\xe4O9Z\x94OZ9\xaaD')
        self.assertEqual( linearcipher(b'Hello', 11, 83), b'k\xaa\xf7\xf7\x18' )

unittest.main()







