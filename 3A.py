sen=input("enter sentence: ")
wl=sen.split()
print("this sentence has ",len(wl)," words")
dc=uc=lc=0
for ch in sen:
    if '0'<=ch<='9':
        dc+=1
    elif 'a'<=ch<='z':
        lc+=1
    elif 'A'<=ch<='Z':
        uc+=1
print("Sentnce contains ",dc,' digits, ',uc,' upper case, ',lc,' lower case')