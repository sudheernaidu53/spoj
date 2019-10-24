class Graph():
    
    def __init__(self, V,adj_list): 
        self.V = V 
        self.adj_list = adj_list
  
    def isBipartite(self): 
        #shifting everything because I am using 1 indexing. as that is better for input
        src = 1
        visited = [0] * (self.V +1)
        visited[0]=1
#         visited[src] = 1
  
        # enqueue source vertex for BFS traversal 
        queue = [] 
#         queue.insert(0,src) 
  
        # to cover all disjoint components, cuz graph can have many components
#         while ((not queue) and visited.index(0)):
        for k in range(1,self.V+1):
            if not visited[k]:
                queue.insert(0,k)
                visited[k]=1
#             queue.insert(0,visited.index(0))
#             visited[visited.index(0)] = 1
            #until queue is empty, BFS)
            while queue:
                u = queue.pop() 

                # Return false if there is a self-loop 
                if u in self.adj_list[u]: 
                    return False

                for v in (self.adj_list[u]): 
#                     print(self.adj_list[u],visited[u],visited[v])
                    if not visited[v]: 

                        # Assign alternate number to this adjacent v of u 
                        visited[v] = -visited[u] 
                        queue.insert(0,v) 

                    elif visited[v] == visited[u]: 
                        return False

        return True
    
# adj_list = [[],[2,3],[1],[1]] 
# g = Graph(3,adj_list) 
def bugging_me(T):
    for test in range(T):
        bugs,relations = map(int,input().strip().split())
        adj_list = [[] for i in range(bugs+1)]
        for i in range(relations):
            a,b = map(int,input().strip().split())
            adj_list[a].append(b)
            adj_list[b].append(a)
        g = Graph(bugs,adj_list)
        print('Scenario #{}:'.format(test+1))
        if g.isBipartite():
            print('No suspicious bugs found!')
        else:
            print('Suspicious bugs found!')
            
    return 
T = int(input())
bugging_me(T)