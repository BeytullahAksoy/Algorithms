def counting_sort(A):# it returns  array B as sorted version of A
    n = len(A)
    k=max(A)
    B=[0 for x in range(0,n)]#this will be sorted array
    C=[0 for x in range(0,k+1)]#place of numbers
    for x in A:
        C[x] +=1
    for y in range(0,len(C)-1):
        C[y+1] += C[y]

    for x in range(n-1,-1,-1):
        print(x)
        place= C[A[x]]-1
        print(place)
        B[place]=A[x]
        C[A[x]]-=1


    return B
A=[2,5,3,0,2,3,0,3]


print(counting_sort((A)))