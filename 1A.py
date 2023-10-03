m1=int(input('enter marks 1:'))
m2=int(input('enter marks 2:'))
m3=int(input('enter marks 3:'))
if(m1<m2):
    if(m1<m3):
        avg=(m3+m2)/2
    else:
        avg=(m1+m2)/2
else:
    if(m2<m3):
        avg=(m1+m3)/2
    else:
        avg=(m1+m2)/2
print(avg)