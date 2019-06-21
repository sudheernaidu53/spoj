def josephmech(n):
    lis = list(range(1,n+1))
    while len(lis)>1:
        if len(lis)%2 == 0:
            lis = lis[::2] #omitting every second number
    #         print(lis) #to check the answer
        elif len(lis)%2 ==1:
            last = lis[-1] #last one won't be killed
            lis = lis[:-2:2]
            lis.insert(0,last) # adding the last to the start
    #         print(lis) #to check the answer
    return lis[0]
def josephbin(n):
    # n=100
    bin_n = bin(n)[2:]
    ans = bin_n[1:]+'1'
    ans = int(ans,base=2)
#     print(ans)
    return ans