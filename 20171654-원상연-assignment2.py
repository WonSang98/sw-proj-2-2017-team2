#팩토리얼 과제
#입력받은 수에 대한 팩토리얼 값 출력
#입력받은 값이 양수가 아닐 때를 고려해야하며, 입력받은 값이 -1일시 실행종료

n = 0

while n is not -1:
    sum = 1
    try :	
        n = int(input("Enter the Positive number. '-1' End on input :  "))
    except ValueError:
        print("정수를 입력하세요")

    if n >=  0:
        for i in range(1,n+1):
            sum*=i
        print(n,"! is ",sum)

    elif n is not -1:
        print("Wrong Input, retry!")
        continue

print("\n The End")
