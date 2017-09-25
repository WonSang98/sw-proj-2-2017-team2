def fac(n):
    #factorial
    if n==1 or n==0 :
        return 1
    else:
        return n*fac(n-1)

def com1(n,r):
    #factorial 을 이용해 조합 구하기
    return fac(n)/fac(n-r)/fac(r)
#이거면 끝..?

def com2(n,r):
    #nCr = n-1Cr + n-1Cr-1을 이용한 재귀함수
    if n==r :
        return 1
    elif r==0:
        return 1
    else:
        return com2(n-1,r) + com2(n-1,r-1)


while True:
    try:
        n,r=int(input("enter n:")),int(input("enter r:"))
    except ValueError :
        print("정수만 입력하세요")
        continue
    
    if n<0 or r<0 :
        print("음수를 입력하지 말아주세요")
        continue
    
    elif n<r :
        print("n>=r 이 되도록 입력해 주세요")
        continue
    #말도안되는 것들을 입력하면 재시작
    
    else:
        print(n,"C",r,"=",com1(n,r),"=",com2(n,r))

        
#에러처리 ->음수, n<r , 정수아님



