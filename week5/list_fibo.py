def fibo_list(n):
    list = [0,1]
    if n < 2:
        return list[n]
    else:
        for i in range(2,n+1):
            list.append(list[i-2]+list[i-1])
        return list[n]

for i in range(10):
    print(fibo_list(i))
