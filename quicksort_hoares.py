def QuickSort(A,p,r): #this calls partition for last number,last number will be middle
    if p<r:           # as [<x][x][>x]. it means x is in its correct position
        q = Partition(A,p,r) # then call left and right part.
        QuickSort(A,p,q-1)
        QuickSort(A, q+1, r)

A=[13,19,9,5,12,8,7,4,11,2,6,21]

def Partition(A,p,r): # [<x][x][>x] and it returns value of middle(the number sorted by)

    i=p-1
    j=r+1
    x=A[p]
    while True:
        j=j-1
        while x<A[j]:
            j=j-1
        i=i+1
        while x >A[i]:
            i=i+1

        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            return j

QuickSort(A,0,len(A)-1)
print(A)
