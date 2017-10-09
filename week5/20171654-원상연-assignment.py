def fibo_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

def fibo(n):

    n1 = 0
    n2 = 1
    result = n1 + n2

    for i in range(1,n):
        result = n1 + n2
        n1 = n2
        n2 = result

    if n == 0:
        return n1
    else:
        return result

import time

while True:
    try:
        n = int(input("몇번째 피보나치를 구하고 싶습니까?\n"))
        if not(n>=0):
            print("음수는 안됩니다.")
            continue
    except (ValueError):
        print("잘못된 입력")
        continue

    s1 = time.time()
    fibo_rec(n)
    e1 = time.time()

    s2 = time.time()
    fibo(n)
    e2 = time.time()

    print(n,"번째 피보나치수열값은", fibo(n))
    print("재귀시간: ", e1-s1)
    print("그냥시간: ", e2-s2)
    print((e1-s1)/(e2-s2),"만큼 빠릅니다.\n")
