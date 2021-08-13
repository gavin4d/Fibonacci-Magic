def fiboArray(n):
    f1 = 1
    f2 = 1
    fibo = [1, 1]
    for i in range (1,n-1):
        sum = f1 + f2
        fibo.append(sum)
        f2 = f1
        f1 = sum
    return fibo


print(fiboArray(5))
