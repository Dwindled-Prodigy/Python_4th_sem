def fib(n):
    a=0
    b=1
    if (n<0):
        print('invalid input')
    elif(n==0):
        return a
    elif(n==1):
        return b
    else:
         return fib(n-1)+fib(n-2)
    
n=int(input('enter number: '))
print(fib(n))
    