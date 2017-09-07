num=input("enter a number")

#int(input())은..정수가 아닌걸 입력해도 정수로 만들어 버려서 뺏음


def fac(num):
    start = 1 #여기에 계속 곱해줘서 ans 가 최종 답이 됨.
    
    if "." in num: #입력한 수가 정수가 아닐때 빠꾸 시킬것임
        
        print("정수만 입력하자..^^*")
        num = input("enter a number") #재입력 시키기
        fac(num) #다시 함수에 넣어줌
        
    else: #입력한 수가 정수일때
        
      num = int(num) #스트링을 정수로 바꿔줌
      
      if num > 0: #양의 정수 일때
          
        for i in range(1,num+1):
            start *= i
            ans = start #결과값
        print(num,"! =",ans) #결과출력
        fac(input("enter a number")) #재 입력받고 다시 함수에 넣음
      
      elif num == -1: 
          print("end") #-1입력시 종료
        
      elif num == 0: 
          print("0! = 1")
          fac(input("enter a number"))
        
      else: #-1아닌 음수 입력시 재입력 
          print("양수입력하자..^^*")
          fac(input("enter a number"))
    


if num != -1:
  fac(num)
else:
    print()


