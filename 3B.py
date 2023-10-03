s1 = input("Enter first string")
s2 = input("Enter second string")
sh = min(len(s1), len(s2))
lo = max(len(s1),len(s2))
x = 0
for i in range (sh):
    if s1[i]==s2[i]:
        x+=1
print('similarity is ',(x/lo))