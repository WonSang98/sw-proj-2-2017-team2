def isNumber(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

while True:
    num=input("Enter a number :")
    if isNumber(num) and int(num)>=-1:
        if int(num)==-1 :
            break
        else :
            ans = 1
            for i in range(1, int(num)):
                ans = ans * (i + 1)
            print(num,end='')
            print('! =',ans)
