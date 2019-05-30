
def endvalue(arr):
    return int(arr[1])
def greedy(chores,startendtimes):
    startendtimes.sort(key = endvalue,reverse = False)
    last_finish = 0
    total = 0
#     schedule = []
#     print('\n',startendtimes,'\n')
    for i in range(chores):
#         print(startendtimes[i][0],last_finish)
        if (int(startendtimes[i][0])>=last_finish):
            last_finish = int(startendtimes[i][1])
#             print(last_finish)
            total+=1
#             schedule.append(startendtimes[i])
#     return schedule,total
    return total

testcase = int(input())
for i in range(testcase):
    chores=int(input())
    startendtimes = [0]*chores
    for i in range(chores):
        startendtimes[i] = (input().strip().split(' '))
    print(greedy(chores,startendtimes))
