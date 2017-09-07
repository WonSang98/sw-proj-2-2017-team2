while True:
    n = int(input('Enter n : '))
    fac = 1
    if n > 1:
        for i in range(1,n+1):
            fac *= i
        print(fac)
    elif n == 0:
        print("fac = 1")
    elif n == -1:
        break
    elif n < 1:
        print("값을 구할수 없음")

    

	    
