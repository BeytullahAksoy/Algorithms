import random

A=[6,4,5,1,2,3,8,7]

def randomized_partition(A,l,r):
    i = random.randrange(r)
    A[i],A[r]=A[r],A[i]
    partition(A,l,r)

def partition(A,l,r):
    if l==r:
        return l
    pivot = A[r]
    i=l-1
    for x in range(l,r):
        if A[x] < pivot:
            A[i+1],A[x]=A[x],A[i+1]
            i+=1
    A[i+1],A[r]=A[r],A[i+1]

def randomized_select(A,l,r,i):
    if r==l:
        return A[r]
    q = randomized_partition(A,l,r)
    if q ==i:
        return A[q]

randomized_partition(A,0,len(A)-1)
print(A)

