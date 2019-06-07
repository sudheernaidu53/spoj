def greedy(s1,s2):
    pointer = 0
    count=0
    if len(s1)<len(s2):
        return len(s1)
    for i in range(len(s1)):
        if s1[i]==s2[pointer]:
#             print('k')
            pointer+=1
            if pointer==len(s2):
#                 print('l')
                pointer=0
                count+=1
    return len(s1)-count*len(s2)
T = int(input())
for i in range(T):
    s1 = input()
    s2 = input()
    print(greedy(s1,s2))