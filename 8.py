class palstr:
    def __init__(self):
        self.ispal=False

    def ckpal(self,mystr):
        if mystr==mystr[::-1]:
            self.ispal=True
        else:
            self.ispal=False
        return self.ispal
    
class palint(palstr):
    def __init__(self):
        self.ispal=False
    
    def ckpal(self,val):
        temp=val
        rev=0
        while(val<0):
            rem=val%10
            rev=(rev*10)+rem
            val=val//10
        if(temp==rev):
            self.ispal=True
        else:
            self.ispal=False
        return self.ispal

st=input('enter word: ')
stobj=palstr()
if stobj.ckpal(st):
    print('palindrome')
else:
    print('not palindrome')

num=int(input('enter number: '))
intobj=palint()
if intobj.ckpal(num):
    print('palandrome')
else:
    print ('not palandrome')