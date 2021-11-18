
import random
def Randomized_QuickSort(A,p,r): # just add this function and this function changes A[r]
    i = random.randrange(p, r)   # with an random number in the array. This function cal
    A[r],A[i] = A[i],A[r]        # calls Partition so call this function in main Quick
    return Partition(A,p,r)      # to get "q".

def QuickSort(A,p,r):
    if p<r:
        q = Randomized_QuickSort(A,p,r)
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