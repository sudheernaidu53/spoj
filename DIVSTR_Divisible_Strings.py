def no_of_letters(string1,string2):
#     print(len(string1),len(string2))
    count = 0 
    pointer = 0
    if len(string1)<len(string2):
        return len(string1)
    if (len(string1)==len(string2)) and (string1!=string2):
        return len(string1)
    for j in range(len(string1)):
        if (string1[j]==string2[pointer]) and pointer<(len(string2)-1):
            pointer+=1
        elif (string1[j]==string2[pointer]) and pointer == (len(string2)-1):
            count+=1
            pointer=0
        elif (string1[j]!=string2[pointer]):
            if string1[j]==string2[0]:
                pointer=1
            else:
                pointer = 0
    return len(string1)-len(string2)*count
T = int(input())
for i in range(T):
    string1 = input()
    string2 = input()
    print(no_of_letters(string1,string2))