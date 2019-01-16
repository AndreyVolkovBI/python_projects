# Main resourse: 
# https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/

# Мостом называется такое ребро, удаление которого делает граф несвязным 
# (или, точнее, увеличивает число компонент связности).
# Требуется найти все мосты в заданном графе.
# Bridges: https://www.geeksforgeeks.org/bridge-in-a-graph/

graph = {"a": ["b", "d"], "b": ["e", "a", "d"], "c": ["f", "e"],
         "d": ["b", "a", "e"], "e": ["d", "c", "b"], "f": ["f", "c"]}
Time = 0
bridges = []

'''A recursive function that finds and prints bridges 
using DFS traversal 
u --> The vertex to be visited next 
visited[] --> keeps tract of visited vertices 
disc[] --> Stores discovery times of visited vertices 
parent[] --> Stores parent vertices in DFS tree'''


def bridgeUtil(u, visited, parent, low, disc):
    global Time
    # Mark the current node as visited and print it
    visited[u] = True

    # Initialize discovery time and low value
    disc[u] = Time
    low[u] = Time
    Time += 1

    # Recur for all the vertices adjacent to this vertex
    for v in graph[u]:
        # If v is not visited yet, then make it a child of u
        # in DFS tree and recur for it
        if not visited[v]:
            parent[v] = u
            bridgeUtil(v, visited, parent, low, disc)

            # Check if the subtree rooted with v has a connection to
            # one of the ancestors of u
            low[u] = min(low[u], low[v])

            ''' If the lowest vertex reachable from subtree 
            under v is below u in DFS tree, then u-v is 
            a bridge'''
            if low[v] > disc[u]:
                bridges.append((u, v))


        elif v != parent[u]:  # Update low value of u for parent function calls.
            low[u] = min(low[u], disc[v])

        # DFS based function to find all bridges. It uses recursive


def bridge(graph):
    # Mark all the vertices as not visited and Initialize parent and visited,
    # and ap(articulation point) arrays
    visited = {vertex: False for vertex in graph}
    disc = {vertex: float("Inf") for vertex in graph}
    low = {vertex: float("Inf") for vertex in graph}
    parent = {vertex: -1 for vertex in graph}

    # Call the recursive helper function to find bridges
    # in DFS tree rooted with vertex 'i'
    for vertex in graph:
        if not visited[vertex]:
            bridgeUtil(vertex, visited, parent, low, disc)

        # Create a graph given in the above diagram


bridge(graph)
print(bridges)


# ===============================================================
# Пусть дан связный неориентированный граф. Точкой сочленения (или точкой артикуляции, англ. "cut vertex" 
# или "articulation point") называется такая вершина, удаление которой делает граф несвязным.
# Cut Vertex: https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/


# Python program to find articulation points in an undirected graph


graph = {"a": ["b", "d"], "b": ["e", "a", "d"], "c": ["f", "e"],
         "d": ["b", "a", "e"], "e": ["d", "c", "b"], "f": ["f", "c"]}
Time = 0
cutVertices = []

'''A recursive function that find articulation points 
using DFS traversal 
u --> The vertex to be visited next 
visited[] --> keeps tract of visited vertices 
disc[] --> Stores discovery times of visited vertices 
parent[] --> Stores parent vertices in DFS tree 
ap[] --> Store articulation points'''


def APVisit(u, visited, ap, parent, low, disc):
    # Count of children in current node
    children = 0

    # Mark the current node as visited and print it
    visited[u] = True

    # Initialize discovery time and low value
    global Time
    disc[u] = Time
    low[u] = Time
    Time += 1

    # Recur for all the vertices adjacent to this vertex
    for v in graph[u]:
        # If v is not visited yet, then make it a child of u
        # in DFS tree and recur for it
        if not visited[v]:
            parent[v] = u
            children += 1
            APVisit(v, visited, ap, parent, low, disc)

            # Check if the subtree rooted with v has a connection to
            # one of the ancestors of u
            low[u] = min(low[u], low[v])

            # u is an articulation point in following cases
            # (1) u is root of DFS tree and has two or more children.
            if parent[u] == -1 and children > 1:
                ap[u] = True

            # (2) If u is not root and low value of one of its child is more
            # than discovery value of u.
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True

        # Update low value of u for parent function calls
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

        # The function to do DFS traversal. It uses recursive APUtil()


def getArticulationPoints():
    # Mark all the vertices as not visited
    # and Initialize parent and visited,
    # and ap(articulation point) arrays
    visited = {vertex: False for vertex in graph}
    disc = {vertex: float("Inf") for vertex in graph}
    low = {vertex: float("Inf") for vertex in graph}
    parent = {vertex: -1 for vertex in graph}
    ap = {vertex: False for vertex in graph}  # To store articulation points

    # Call the recursive helper function
    # to find articulation points
    # in DFS tree rooted with vertex 'i'
    for vertex in graph:
        if not visited[vertex]:
            APVisit(vertex, visited, ap, parent, low, disc)

    return ap

def prettyPrint(ap):
    print("Articulation points")
    for cut in ap:
        if ap[cut]:
            print(cut)


ap = getArticulationPoints()
prettyPrint(ap)

