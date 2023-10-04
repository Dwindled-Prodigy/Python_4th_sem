def b2d(b):
    d,i=0,0
    while(b!=0):
        dec=b%10
        d=d+dec*pow(2,i)
        b=b//10
        i+=1
    return d

num=int(input("enter binary: "))
print(b2d(num))
