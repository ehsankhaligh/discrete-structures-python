#Ehsan Hosseinzadeh Khaligh
def gcd(x, y):

    while(y):
        x, y = y , x % y  
    return x

def lcm(a, b):
    
    return abs(a*b) / gcd(a,b)

def egcd(a, b):
    
    if b == 0:
        return (1, 0)

    else:
        q = a // b
        r = a % b

        (s, t) = egcd(b, r)

        return (t, s - q * t)

def multinv(m, n):
    
    (x, y) = egcd(m, n)

    return x % n
        
def decrypt(m, e, k):

    return (e-k) * multinv(m, 256) % 256


def linearcipher(bstr, m, k):

    return bytes( [ (m*b+k) % 256 for b in bstr] )


def lineardecipher(lstr, m, k):
    
    return bytes ( (decrypt (m, e, k) ) for e in lstr)

import unittest


class MyTest(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual( gcd(42, 35) , 7 )
        self.assertEqual( gcd(37, 16) , 1 )
        self.assertEqual( gcd(52, 81), 1 )
        self.assertEqual( gcd(10, 15), 5 )
        self.assertEqual( gcd(5,5), 5)

    def test_lcm(self):
        self.assertEqual( lcm(3,1) , 3 )
        self.assertEqual( lcm(5,0) , 0 )
        self.assertEqual( lcm(11, 3), 33 )
 

    def test_egcd(self):
        self.assertEqual( egcd(6, 4) , (1, -1)  )
        self.assertEqual( egcd(6, 3) ,  (0, 1) )
        self.assertEqual(  egcd(9,6), (1,-1) )


    def test_multinv(self):
        self.assertEqual( multinv(15, 26) , 7 )
        self.assertEqual( multinv(7,26), 15 )


    def test_linearcipher(self):
        self.assertEqual(linearcipher(b'Hello Sierra', 5, 11), b"s\x04''6\xab\xaa\x18\x04EE\xf0")
        self.assertEqual(linearcipher(b'Discrete Structures', 11, 83), b'?\xd6D\x949\xaaO\xaa\xb3\xe4O9Z\x94OZ9\xaaD')
        self.assertEqual(linearcipher(b'Sierra', 11, 83), b'\xe4\xd6\xaa99~')

    def test_lineardecipher(self):
        self.assertEqual(lineardecipher(b"s\x04''6\xab\xaa\x18\x04EE\xf0", 5, 11), b'Hello Sierra')
      


    def test_decrypt(self):
        self.assertEqual( decrypt(5, 61, 11), 10)
        self.assertEqual( decrypt(5, 80, 11), 65)
        self.assertEqual( decrypt(5, 149, 11), 130)

unittest.main()




