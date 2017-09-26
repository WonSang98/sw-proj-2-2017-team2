#팩토리얼 재귀함수
def fac(x):
    if x == 1:
        return 1
    return x*fac(x-1)

#팩토리얼 함수를 이용한 조합
#각각의 팩토리얼을 구해서 계산한 값을 리턴
def nCk(n, k):
    return fac(n)/(fac(k)*fac(n-k))

#조합 재귀함수
def comb(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    else:
        return (n/k)*comb(n-1, k-1)
