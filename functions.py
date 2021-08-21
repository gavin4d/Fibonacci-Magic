def fiboarray(n):
    fibo = [0,1]
    for i in range (2,n):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo

def fiboarray_extended(a,b):
    max_fibo = fiboarray(max(abs(a),abs(b))+1)
    
    output = []

    for i in range (a,b):
        if (i < 0):
            output.append(-int(pow(-1,i)) * max_fibo[-i])
        else:
            output.append(max_fibo[i])
    return output

#print(fiboarray(int(input())))
#print(fiboarray_extended(int(input()),int(input())))