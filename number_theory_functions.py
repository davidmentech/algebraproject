from random import randrange

def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 


def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if a == 0 :
        return b,0,1        
    gcd,x1,y1 = extended_gcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1  
    return gcd,x,y




def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """


def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result

def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
        
    binaryrep=bin(d)
    a1=a%n
    degree=0
    sum=1
    for  i in binaryrep[-1:1:-1]:
        
        sum *= (a1**(int(i)*(2**degree)))%n
        degree += 1
    return sum%n

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None

def task1():
    gcd,x,y=extended_gcd(911,7879)
    if((10**6)%gcd==0):
        print(gcd)
        x1=((x)*10**6//gcd)
        y1=(y*10**6//gcd)
        s='911*'+str(x1)+'+7879*'+str(y1)+'=10^6'
        print(s)

def task2():
    k=phi(1000)
    sum1=modular_exponent(7896543,74365753%phi(k),k)
    #print(modular_exponent(456457,sum1,1000)//100)
    print(modular_exponent(143,153,400))
    print(modular_exponent(457,143,1000))


if __name__=="__main__":
    #task1()
    task2()



