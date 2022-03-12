def solution(entrances, exits, path):
    graph=deep_copy(path)
    #print(graph)
    flow=0
    counter=0
    while True:
        counter+=1
        #find a path 
        t=find_path(entrances,graph,exits)
        if(t==-1):
            return flow
        else:
            #(path in reverse,capacities)
            (l,w)=t
            #print(l,w)
            #addition to flow
            df=min(w)
            #print(df)
            flow+=df
            #change graph
            for i in range(len(l)-1):
                graph[l[i]][l[i+1]]+=df
                graph[l[i+1]][l[i]]-=df
            #print(graph)

#make a graph deep copy to play with
def deep_copy(g):
    graph=[]
    for i in range(len(g)):
        graph.append([])
        for j in range(len(g[i])):
            graph[i].append(g[i][j])
    return graph
#-----------------------------------

# depth first search from v until an exit
def dfs(v,graph,stop_nodes): 
    l=[]
    weights=[]
    visited=set()
    def dfs_recursion(v,prev):

        if(v in stop_nodes):
            l.append(v)
            weights.append(graph[prev][v])
            return True

        for i,u in enumerate(graph[v]):
            
            if(u>0 and (i not in visited)):
                visited.add(i)
                if(dfs_recursion(i,v)): 
                    l.append(v)
                    weights.append(graph[prev][v])
                    return True
                    
        return False
    dfs_recursion(v,-1)
    return l,weights[:-1]
#----------------------------------------

# find path from entrances to exits -----

def find_path(entrances,graph,exits):
    for e in entrances:
        (l,w)=dfs(e,graph,exits)
        if(l!=[]):
            return (l,w)
    return -1

# ---------------------------------------


g=[[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
en=[0, 1]
ex=[4, 5]

#print(dfs(0,g,ex))
#print(dfs(1,g,ex))

#print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
#print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
#print(find_path(en,g,ex))