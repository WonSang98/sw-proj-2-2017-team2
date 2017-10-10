while True:
    try:
     print("Enter n : ",end="")
     n=int(input())
     if n>=0:
        print("Enter m : ",end="")
        m = int(input())
        if m>=0:
            ans=1
            wer=1
            result=1
            for i in range(1, n+1):
                ans *= i
            for i in range(1, m+1):
                wer *= i
            for i in range(1, n-m+1):
                result *= i
            last = ans/wer/result
            print(n,"C",m," = ",last)

        else:
            print("Please enter positive number")
     else:
        print("Please enter positive number")
    except:
        print("Error \nPlease enter positive number")