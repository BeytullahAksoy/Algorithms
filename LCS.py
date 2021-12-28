import pdb
# The LCS method returns b and c table for longest common subsequent between two strings.
# The b array shows next indexes for the subsequence.

def LCS(X,Y):
    m = len(X)
    n = len(Y)
    c = [[0 for x in range(n+1)] for y in range(m+1)]
    b = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(1,len(X)+1):
        for j in range(1,len(Y)+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = 1 + c[i-1][j-1]
                b[i][j] = f"{i-1} , {j-1}"
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = f"{i} , {j-1}"
            elif c[i][j-1]>c[i-1][j]:
                c[i][j] = c[i][j-1]
                b[i][j] = f"{i-1} , {j}"
    return c,b

def reconstruct_LCS(c,X,Y): # O(m+n)time, without using the b table.
    i = len(X)
    j = len(Y)
    subsequence = []
    while True:

        if X[i-1] == Y[j-1]:
            subsequence.append(X[i-1])
            i-=1
            j-=1
        elif c[i][j-1]>=c[i-1][j]:
            j-=1
        elif c[i-1][j]>=c[i][j-1]:
            i-=1
        if i==0 or j==0:
            break
    return subsequence[::-1]



X = list("BDCABA")
Y = list("ABCBDAB")

c,b = LCS(X,Y)
#print(c)
print(reconstruct_LCS(c,X,Y))