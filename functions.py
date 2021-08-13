def fiboarray(n):
    f1 = 0
    f2 = 1
    fibo = [0]
    for i in range (1,n):
        sum = f1 + f2
        fibo.append(sum)
        f2 = f1
        f1 = sum
    return fibo


print(fiboarray(10))
