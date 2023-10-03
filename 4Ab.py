import random
def IS(arr):
    for s in range (len(arr)):
        k=arr[s]
        j=s-1
        while j>=0 and k<=arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=k
list=[]
for i in range (10):
    list.append(random.randint(0,99))
print('unsorted list')
print(list)
IS(list)  
print("Sorted List")
print(list)