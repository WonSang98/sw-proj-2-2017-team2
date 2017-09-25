def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

def combine_fac(n,m):
    return fac(n)/(fac(m)*fac(n-m))

def combine(n, m): #n >= m
    nf = 1
    mf = 1
    if n == m and m == 0:
        return 1
    elif n < m:
        return False
    else:
        for i in range(m):
            nf *= (n-i)
            mf *= (i+1)
        return nf/mf
