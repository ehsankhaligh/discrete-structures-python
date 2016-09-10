import sys
sys.setrecursionlimit(10000)


def ifac(n):
        prad = 1
        for i in range(1, n+1):
                prad = prad * i

        return prad

def rfac(n):
        if n == 0:
                return 1
        else:
                return n * rfac(n-1)


def perm(n,r):
    
    return rfac(n)// rfac(n-r)

def comb(n,r):
    
    return rfact(n)// (rfact(n-r * rfact(r)))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# Dic 
fmemo = {}   
def mfib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if n in fmemo:
            return fmemo [n]
        else:
            res = mfib(n-1)+ mfib(n-2)
            fmem[n] = res
            return res

pmemo = {}         
def pascal(r, c):
    if c == 0:
        return 1
    elif r==c:
        return 1
    else:
         if (r,c) in pememo:
             return pmemo[(r,c)]
         else:
             res = pascal (r-1, c-1) +  pascal(r -1, c)
             pmemo[(r,c)] = res
             return res 


def mpascal(r, c):
    if c==0:
        return 1
    elif r==c:
        return 1
    else:
         return mpascal (r-1, c-1) +  mpascal(r -1, c)



