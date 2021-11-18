def QuickSort(A,p,r): #this calls partition for last number,last number will be middle
    if p<r:           # as [<x][x][>x]. it means x is in its correct position
        q = Partition(A,p,r) # then call left and right part.
        QuickSort(A,p,q-1)
        QuickSort(A, q+1, r)

A=[2,8,7,1,3,5,6,4]


def Partition(A,p,r): # [<x][x][>x] and it returns value of middle(the number sorted by)
    pivot = A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<pivot:
            A[i+1] , A[j] = A[j],A[i+1]
            i=i+1
    A[i+1] , A[r] = A[r],A[i+1]
    return i+1


QuickSort(A,0,len(A)-1)
print(A)