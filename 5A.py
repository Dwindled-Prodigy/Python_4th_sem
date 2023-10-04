import re
def isPH(numstr):
    if len(numstr)!=12:
        return False
    for i in range (len(numstr)):
        if i==3 or i==7:
            if numstr[i]!='-':
                return False
        else:
            if numstr[i].isdigit()==False:
                return False
    return True

def chkpn(numstr):
    ph_pt=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_pt.match(numstr):
        return True
    else:
        return False
    
ph_num=input("enter a phone number")
print("without using Regular Expression")
if isPH(ph_num):
    print ("valid phone number")
else:
    print('Invalid phone number')
print ('using regular expression')
if chkpn(ph_num):
    print("Valid Phone Number")
else:
    print("invalid phone number")
