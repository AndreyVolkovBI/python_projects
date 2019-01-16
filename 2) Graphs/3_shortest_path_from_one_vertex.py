# Дан ориентированный или неориентированный взвешенный граф с n вершинами и m рёбрами. 
# Веса всех рёбер неотрицательны. Указана некоторая стартовая вершина s. Требуется найти 
# длины кратчайших путей из вершины s во все остальные вершины, а также предоставить способ вывода самих кратчайших путей.
# single-source shortest paths problem

# ===============================================================
# Adjacency matrix representation
# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
# Source:  https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/


def printSolution(dist):
    print("Vertex tDistance from Source")
    for node in range(len(graph)):
        print(node, "t", dist[node])


# A utility function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree
def minDistance(dist, sptSet):
    # Initialize minimum distance for next node
    min = float("inf")

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(len(graph)):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index


# Function that implements Dijkstra's single source
# shortest path algorithm for a graph represented
# using adjacency matrix representation
def dijkstra(src):
    V = len(graph)
    dist = [float("inf")] * V
    dist[src] = 0
    sptSet = [False] * V

    for count in range(V):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shortest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for v in range(V):
            if graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


# graph - [[]] симметричная матрица где нам показаны вершины графа от нуля до максимума
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]

dist = dijkstra(0)  # returns the shortest path from vertex 0
printSolution(dist)  # prints existing solution


# ===============================================================
# Adjacency printing paths representation
# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph
# Source: https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/

# A utility function to find the
# vertex with minimum dist value, from
# the set of vertices still in queue
def minDistance(dist, queue):
    # Initialize min value and min_index as -1
    minimum = float("Inf")
    min_index = -1

    # from the dist array,pick one which
    # has min value and is till in queue
    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index


# Function to print shortest path
# from source to j
# using parent array
def printPath(parent, j):
    # Base Case : If j is source
    if parent[j] == -1:
        print(j)
        return

    printPath(parent, parent[j])
    print(j)


# A utility function to print
# the constructed distance
# array
def printSolution(dist, parent):
    src = 0
    print("Vertex \t\tDistance from Source\tPath")
    for i in range(1, len(dist)):
        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]))
        printPath(parent, i)


'''Function that implements Dijkstra's single source shortest path 
algorithm for a graph represented using adjacency matrix 
representation'''


def dijkstra(graph, src):
    row = len(graph)
    col = len(graph[0])

    # The output array. dist[i] will hold
    # the shortest distance from src to i
    # Initialize all distances as INFINITE
    dist = [float("Inf")] * row

    # Parent array to store
    # shortest path tree
    parent = [-1] * row

    # Distance of source vertex
    # from itself is always 0
    dist[src] = 0

    # Add all vertices in queue
    queue = []
    for i in range(row):
        queue.append(i)

    # Find shortest path for all vertices
    while queue:

        # Pick the minimum dist vertex
        # from the set of vertices
        # still in queue
        u = minDistance(dist, queue)

        # remove min element
        queue.remove(u)

        # Update dist value and parent
        # index of the adjacent vertices of
        # the picked vertex. Consider only
        # those vertices which are still in
        # queue
        for i in range(col):
            '''Update dist[i] only if it is in queue, there is 
            an edge from u to i, and total weight of path from 
            src to i through u is smaller than current value of 
            dist[i]'''
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = dist[u] + graph[u][i]
                    parent[i] = u

                # print the constructed distance array
    printSolution(dist, parent)


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]

# Print the solution
dijkstra(graph, 0)

