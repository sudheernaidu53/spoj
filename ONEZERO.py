
from collections import deque

def find_onezero(num):
    edges = [[0,1],[0,1]]
    start = 1
    nodes = deque()
    nodes.append([1,1])
    while nodes:
        curr_node = nodes.popleft()
        if not(curr_node[1]%num):
            return curr_node[1]
        else: 
            for node in edges[curr_node[0]]:
                nodes.append([node,(curr_node[1])*10+node])
                
T = int(input())
for test in range(T):
    print(find_onezero(int(input())))