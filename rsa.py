import gmpy2

def decrypt(N, d, c):
    m = pow(c, d, N)
    return m

def crack(N, e, c, factor_function):
    factors = factor_function(N)
    if factors == None:
        return None

    p, q = factors
    assert p*q == N

    totient = (p - 1)*(q - 1)
    d = gmpy2.invert(e, totient)
    return decrypt(N, d, c)