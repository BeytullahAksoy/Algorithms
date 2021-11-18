A=[5,2,4,6,1,3]
def insertion_sort(A):
    r=len(A)
    for i in range(1,r):
        j=i-1
        key=A[i]
        while key<A[j] and j>=0 :
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
insertion_sort(A)
print(A)
