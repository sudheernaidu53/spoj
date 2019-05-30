# ps: this solution was not accepted by spoj because this solution crossed the time limit
def findmaxden(denominations):
    if len(denominations)<2:
        return len(denominations)
    denominations.sort()
#     denominations = sorted(denominations)
    total = denominations[0]
    count = 1
    for i in range(1,len(denominations)-1):
        if (total+denominations[i]>denominations[-1]):
            return count+1
        if (total+denominations[i]<denominations[i+1]):
            count+=1
            total+=denominations[i]
    return count+1
T = int(input())
for i in range(T):
    N = int(input())
    denominations = [int(i) for i in input().strip().split()]
    print('Case #{}: {}'.format(i+1,findmaxden(denominations)))