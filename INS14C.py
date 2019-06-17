
def greedybin(binary,start,end):
    if start==end:
        return binary
    binary = list(binary)
    for i in range(0,start-end,2):
        try:
            binary.remove('1')
        except:
            binary.remove('0')
        # print('yay',binary)
    for i in range(1,start-end,2):
        try:
            binary.remove('0')
        except:
            binary.remove('1')
    return ''.join(binary)
T = int(input())
for i in range(T):
    start,end = map(int, input().split())
    binary = input()
    print(greedybin(binary,start,end))