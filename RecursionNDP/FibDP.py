

fib= {}
fib[1] = fib[0] = 1
def fibo(i):
    for n in range(2,i+1):
        fib[n]  = fib[n-1] + fib[n-2]
    return fib[i]

print fibo(200)


    
