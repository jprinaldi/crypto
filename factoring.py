import gmpy2

# Factor N when abs(p - q) < 2*pow(N, 0.25)
def factor_1(N):
    A = gmpy2.isqrt(N) + 1
    x = gmpy2.isqrt(A*A - N)
    p = A - x
    q = A + x

    if p*q == N:
        return p, q
    else:
        return None

# Factor N when abs(p - q) < pow(2, 11)*pow(N, 0.25)
def factor_2(N):
    initial_A = gmpy2.isqrt(N)
    A = initial_A
    upper_bound = pow(2, 20)

    while A - initial_A < upper_bound:
        A += 1
        x = gmpy2.isqrt(A**2 - N)
        p = A - x
        q = A + x

        if p*q == N:
            return p, q

    return None

# Factor N when abs(3*p - 2*q) < pow(N, 0.25)
def factor_3(N):
    B = gmpy2.isqrt(24*N) + 1
    x = gmpy2.isqrt(B**2 - 24*N)
    p = (B - x)/6
    q = (B + x)/4

    if p*q == N:
        return p, q
    else:
        return None