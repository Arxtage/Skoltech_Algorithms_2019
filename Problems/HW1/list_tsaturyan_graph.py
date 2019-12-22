from heapq import heappush, heappop

def my_dijkstra_heap(graph, start, d):
    dist = {}
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if v not in dist:
            if path_len <= d:
                dist[v] = path_len
                try:
                    graph[v].items()
                    if len(graph[v].items()) != 0:
                        for w, edge_len in graph[v].items():
                            if w not in dist:
                                heappush(queue, (path_len + edge_len, w))
                except: pass
                                
    return (dist)
    
def main():
    
    graph = {}
    graph_r = {}
    
    edges = set()
    inp = input().split()

    for i in range(int(inp[1])):
        line = input().split()
        if int(line[0]) in graph:
            # append the new number to the existing array at this slot
            graph[int(line[0])].update({int(line[1]):int(line[2])})
        else:
            # create a new array in this slot
            graph[int(line[0])] = {int(line[1]):int(line[2])}
            
        if int(line[1]) in graph_r:
            # append the new number to the existing array at this slot
            graph_r[int(line[1])].update({int(line[0]):int(line[2])})
        else:
            # create a new array in this slot
            graph_r[int(line[1])] = {int(line[0]):int(line[2])}
        
        
        edges.add(int(line[0]))
        edges.add(int(line[1]))
    
    for i in edges:
        try:
            graph[i]
        except:
            graph[i] = {}
        
        try:
            graph_r[i]
        except:
            graph_r[i] = {}
    
    s, t, d = input().split()
    s = int(s)
    t = int(t)
    d = int(d)
    
    count = 0

    s_dijkstra = my_dijkstra_heap(graph,s,d)
    
    try:
        res = s_dijkstra[t]
        print(int(inp[0])**2 - int(inp[0]))
        return()
    except:
        t_dijkstra = my_dijkstra_heap(graph_r,t,d)
        s_dists = list(s_dijkstra.values())
        t_dists = list(t_dijkstra.values())
        
        go = len(t_dists) - 1
        for i in range(len(s_dists)):
            while go >= 0 and s_dists[i] + t_dists[go] + 1 > d:
                go -= 1
            count += go+1
        print(count)
        
        
if __name__== "__main__":
    main()