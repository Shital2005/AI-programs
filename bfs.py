graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)  # Mark the node as visited
    queue.append(node)  # Add the node to the queue

    while queue:  # While there are nodes in the queue
        m = queue.pop(0)  # Dequeue a node from the queue
        print(m, end=" ")  # Print the node

        for neighbour in graph[m]:  # Iterate through the neighbours of the dequeued node
            if neighbour not in visited:  # If the neighbour has not been visited
                visited.append(neighbour)  # Mark it as visited
                queue.append(neighbour)  # Enqueue it

print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')  # Start BFS from node 'A'

