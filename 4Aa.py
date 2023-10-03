import random
def MS(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        L = arr[:r]
        M = arr[r:]
        MS(L)
        MS(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1

def printlist(arr):
    for i in range(len(arr)):
        print(str(arr[i]), end=" ")
    print()

if __name__ == '__main__':
    my_list = []
    for i in range(10):
        my_list.append(random.randint(0, 99))
    print('The unsorted array is:')
    printlist(my_list)
    MS(my_list)
    print('The sorted array is:')
    printlist(my_list)