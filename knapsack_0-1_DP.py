def kp_01_dp(vals,wts,cap):
    t = [[0 for x in range(cap+1)] for x in range(len(wts))]
    for x in range(len(vals)):
        for y in range(cap+1):
            if x==0 or y == 0:
                t[x][y] = 0
            elif wts[x] <= y:
                t[x][y] = max(vals[x]+t[x-1][y-wts[x]],t[x-1][y])
            else:
                t[x][y] = t[x-1][y]
    return t[len(vals)-1][cap]




vals = [0,1,2,5,6]
wts = [0,2,3,4,5]
print(kp_01_dp(vals,wts,8))