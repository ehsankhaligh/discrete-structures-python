import random

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def egcd(a,b):
    if b==0:
        return(1,0)
    else:
        q = a//b
        r =a % b
        (s,t) = egcd(b,r)
        return(t, s - q *t)

def multinv(a,n):
    (x,y) = egcd(a,n)
    return x % n
    
    
def n(p,q):
    return p*q

def phi(p,q):
    return (p-1)*(q-1)

def e(phi1):
    all_e = [ e for e in range(2, phi1) if gcd(e, phi1)==1]
    #idx = random.randrange(0, len(all_e))
    return all_e
    #all_e[idx]

def d(e,phi1):
    return multinv(e, phi1)
    
def genkey(p,q):
    n1 = n(p,q)
    phi1 = phi(q,p)
    e1 = e(phi1)
    d1 = d(e1, phi1)
    return( (e1, n1), (d1,n1) )


def rsa(msg, exp, modulus):
    return pow(msg, exp, modulus)

def encrypt(bstr, exp, modulus):

    return [rsa(b, exp, modulus) for b in bstr]

def decrypt(arr, exp, modulus):

    return bytes( [rsa(a, exp, modulus) for a in arr] ) 
