def greedy(wine):
    n = len(wine)
    work =0
    for i in range(n-1):
        wine[i+1]+=wine[i]
        work += abs(wine[i])
#         print(work)
#         print(wine)
    return work
while(1):
    if int(input())!=0:
        arr = [int(i) for i in input().strip().split()]
        print(greedy(arr))
    else:break