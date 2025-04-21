graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}

visited =[]
def dfs(visited, graph, node) :
    if node not in visited:  # If the node has not been visited
        print(node)  # Print the node
        visited.append(node)  # Mark it as visited

        for neighbour in graph[node]:  # Iterate through the neighbours of the node
            dfs(visited, graph, neighbour)  # Recursively call DFS for each neighbour
dfs(visited,graph,'A')            