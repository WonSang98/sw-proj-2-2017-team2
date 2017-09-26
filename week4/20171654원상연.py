#20171654
#WonSang98 원상연
#Week4 Assignment
#Fatorial fuction & Combine factorial ver, recursive ver

def fac(n):#Fatorial Recursive
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)

def combine_fac(n, m):#Combine Factorial ver
    return fac(n)/(fac(m)*fac(n-m))

def combine_rec(n, m):#Combine Recursive ver
    if m == 1 or n == m :
        return n/m
    elif m > n:
        return False
    else:
        return int((n/m)*combine_rec(n-1, m-1))


def combine(n, m):#Combine Just
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
        return int(nf/mf)
