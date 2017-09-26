import time

def combine_rec(n, m):#Combine Recursive ver
    if m == 1 or n == m :
        return n/m
    elif m > n:
        return False
    else:
        return int((n/m)*combine_rec(n-1, m-1))

def com2(n,r):
    #nCr = n-1Cr + n-1Cr-1을 이용한 재귀함수
    if n==r :
        return 1
    elif r==0:
        return 1
    else:
        return com2(n-1,r) + com2(n-1,r-1)

start_time1 = time.time()

print(combine_rec(24,13))

end_time1 = time.time()

print(end_time1-start_time1)

start_time2 = time.time()

print(com2(24,13))
end_time2 = time.time()

print(end_time2-start_time2)
