import sys
A =[1,-3,2,4,5,12,-4,13,11,8]

def max_sub(A,low,mid,high):
    leftSum = -sys.maxsize
    sum =0

    for x in range(mid,low,-1):
        sum = sum + A[x]
        if sum > leftSum:
            leftSum=sum
    rightSum = -sys.maxsize
    sum = 0

    for x in range(mid+1,high+1):
        sum = sum + A[x]
        if sum > rightSum:
            rightSum=sum

    return  leftSum , rightSum , leftSum+rightSum

def max_sub_call(A,low,high):
    if low >=high:
        return low
    else:
        leftSum = max_sub(A,low,int((low+high)/2),high)[0]
        rightSum = max_sub(A, low, int((low + high) / 2), high)[2]
        acrossSum = max_sub(A, low, int((low + high) / 2), high)[1]
        print(leftSum)
        print(rightSum)
        print(acrossSum)

    return max(leftSum,rightSum,acrossSum)
print(max_sub_call(A,0,9))