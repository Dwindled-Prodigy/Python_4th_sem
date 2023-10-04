def o2h(n):
    rev=n [::-1]
    i=dec=0
    for dig in rev:
        dec+=int(dig)*8**i
        i+=1
    list=[]
    while(dec!=0):
        list.append(dec%16)
        dec=dec//16
    a=[]
    for elem in list[::-1]:
        if elem<=9:
            a.append(str(elem))
        else:
            a.append(chr(ord('A')+(elem-10)))
    hex=" ".join(a)
    return hex

num=int(input('enter octal: '))
print(o2h(num))