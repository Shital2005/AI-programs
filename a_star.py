import heapq

def a_star(graph,heuristic, start, goal):
    open_list = [(heuristic[start],0,start,[start])]
    g_scores = {start: 0}  # Cost from start to the current node

    while open_list:
        f,g,node,path = heapq.heappop(open_list)  # Get the node with the lowest f score
        if node == goal:
            print("Path:","->".join(path))
            print("Total Cost:", g)
            return g
        for neighbour, cost in graph[node].items():
            g_new = g + cost
            if neighbour not in g_scores or g_new < g_scores[neighbour]:
                g_scores[neighbour] = g_new
                f_new = g_new + heuristic[neighbour]
                heapq.heappush(open_list, (f_new, g_new, neighbour, path + [neighbour]))

    return float('inf')  # Return infinity if no path is found





graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

cost = a_star(graph, heuristic, 'A', 'E')
print("Total Cost:", cost)
