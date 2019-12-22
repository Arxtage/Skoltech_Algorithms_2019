from heapq import heappush, heappop
import copy



def my_dijkstra_heap(G,s):
    
    s_index = s-1 #work with right indexing, node #1 now is #0   
    queue = [(0, s_index)]
    
    dist = [1000000001] * len(graph)
    dist[s_index] = 0
    
    while queue:
        path_len, u = heappop(queue)
        for v in range(len(G[u])):
            if G[u][v]:
                if dist[v]>dist[u]+G[u][v]:
                    dist[v] = dist[u]+G[u][v]
                    heappush(queue,(dist[v], v))
    return(dist)

def bi_dijkstra(G,s,t,d):
 
 
    s_index = s-1 #work with right indexing, node #1 now is #0
    t_index = t-1
    
    dist = [1000000001] * len(graph)
    dist_r = [1000000001] * len(graph)
    dist[s_index] = 0    
    dist_r[t_index] = 0

    queue = [(0, s_index)] 
    queue_r = [(0, t_index)]

    relaxes = set()
    relaxes_r = set()
    
    while queue and queue_r:
        
        _ , u = heappop(queue)
        _ , u_r = heappop(queue_r)
        
        relaxes.add(u)
        relaxes_r.add(u_r)
        
        if (relaxes & relaxes_r):
            for i in relaxes & relaxes_r:
                if(dist[i]+dist_r[i]<=d):
                    return(True)
        
        for v in range(len(G[u])):
            if G[u][v]:
                if dist[v]>dist[u]+G[u][v]:
                    dist[v] = dist[u]+G[u][v]
                    heappush(queue,(dist[v], v))
                    
        for v_r in range(len(G[u_r])):
            if G[v_r][u_r]:
                if dist_r[v_r]>dist_r[u_r]+G[v_r][u_r]:
                    dist_r[v_r] = dist_r[u_r]+G[v_r][u_r]    
                    heappush(queue_r,(dist_r[v_r], v_r))
    return(False)
 
def main():
    
    inp = input().split()
 
    graph = [[0 for x in range(int(inp[0]))] for y in range(int(inp[0]))] 
 
    for i in range(int(inp[1])):
        line = input().split()
        graph[int(line[0])-1][int(line[1])-1] = int(line[2]) #-1 bcs count from 0 in array, while vertices from 1 
    s, t, d = input().split()
    s = int(s)
    t = int(t)
    d = int(d)
 
    count = 0
    result = 0
    s_dijkstra = my_dijkstra_heap(graph,s)
    t_dijkstra = my_dijkstra_heap(list(map(list, zip(*graph))),t)

    if s_dijkstra[t-1]<=d:
        print(len(graph)**2 - len(graph))
        return()
    s_indexes =set()
    t_indexes =set()

    for ind, dis in enumerate(s_dijkstra):
        if dis <= d or dis == 1000000001:
            s_indexes.add(ind)
    for ind, dis in enumerate(t_dijkstra):
        if dis <= d or dis == 1000000001:
            t_indexes.add(ind)
        
    for i in s_indexes:
        for j in t_indexes:
            if i == j:
                continue
            mind = copy.copy(graph[i][j])
            graph[i][j] =1
            result = bi_dijkstra(graph,s,t,d)
            graph[i][j] = mind
            if (result):
                count +=1
    print(count)
 
 
if __name__== "__main__":
    main()