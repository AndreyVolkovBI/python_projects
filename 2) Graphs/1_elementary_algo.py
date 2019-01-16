Adj = {"a": ["b", "d"], "b": ["e"], "c": ["f", "e"], "d": ["b"], "e": ["d"], "f": ["f"]}

# Main resourse: 
# https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/

# BFS - breadth first search: finds the shortest path from one point to another
# Note that bfs do not explore the whole graph, it only finds all the ways reachable from one vertex - s
# Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

def bfs(s, Adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    return parent, level


parent, level = bfs("a", Adj)

# DFS - depth first serach: explores the whole graph, visiting all the vertices
# returns the way from one point to another (not the shortest, but the most obvious one)
# Source: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
parent = {}

def dfs_visit(s, Adj):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(v, Adj)

def dfs(Adj):
    for s in Adj:
        if s not in parent:
            parent[s] = None
            dfs_visit(s, Adj)

#v = [vertex for vertex in Adj]
dfs(Adj)  # giving list of all the vertices, dict of adjacencies


# Topological sort - топологическая сортировка сети (ориентированный граф)
# указать такой линейный порядок на его вершинах, чтобы любое ребро 
# вело от вершины с меньшим номером к вершине с большим номером.
# Source: https://www.geeksforgeeks.org/topological-sorting/

# Color - массив, в котором хранятся цвета вершин (0 — белый, 1 — серый, 2 — черный).
# Edges - массив списков смежных вершин.
# Numbers - массив, в котором сохраняются новые номера вершин.
# Stack - стек, в котором складываются вершины после их обработки.
# Cycle - принимает значение true, если в графе найден цикл.
edges = {'a': ['c'], 'c': ['b'], 'd': ['c', 'b', 't'], 'b': [], 't': []}


def dfs(color, stack, v):
    # Если вершина серая, то мы обнаружили цикл.
    # Заканчиваем поиск в глубину.
    if color[v] == 1:
        return True
    if color[v] == 2:
        return False  # Если вершина черная, то заканчиваем ее обработку.
    color[v] = 1  # Красим вершину в серый цвет.
    # Обрабатываем список смежных с ней вершин.
    for i in range(len(edges[v])):
        if dfs(color, stack, edges[v][i]):
            return True
    stack.append(v)  # Кладем вершину в стек.
    color[v] = 2  # Красим вершину в черный цвет.
    return False


def topological_sort(stack, color):
    # Вызывается обход в глубину от всех вершин.
    # Заканчиваем работу алгоритма, если обнаружен цикл.
    for i in edges:
        cycle = dfs(color, stack, i)
        if cycle:
            print("Cycle!")
            exit()

    # Заносим в массив новые номера вершин.
    stack.reverse()
    return stack


topologicallySortedList = topological_sort(stack=[], color={vertex: 0 for vertex in edges}) 


# Алгоритм поиска компонент связности в графе - Connected Components
# Возвращает все окмпоненты связности
# Note that it algo works in undirected graphs only!
# Bi-connected components: https://www.geeksforgeeks.org/biconnected-components/
# Source: https://www.geeksforgeeks.org/strongly-connected-components/

Adj = {"a": ["b", "d"], "b": ["e", "a", "d"], "c": ["f", "e"],
       "d": ["b", "a", "e"], "e": ["d", "c", "b"], "f": ["f", "c"]}


def DFS(component, vertex, visited):
    # Mark the current vertex as visited
    visited[vertex] = True
    # Store the vertex to list
    component.append(vertex)
    # Repeat for all vertices adjacent
    # to this vertex v
    for u in Adj[vertex]:
        if not visited[u]:
            # Update the list
            component = DFS(component, u, visited)
    return component


# Method to retrieve connected components
# in an undirected graph
def getConnectedComponents():
    visited = {vertex: False for vertex in Adj}  # {name_of_vertex: False/True}
    connectedComponents = []
    for vertex in Adj:
        if not visited[vertex]:
            connectedComponents.append(DFS(component=[], vertex=vertex, visited=visited))
    return connectedComponents


cc = getConnectedComponents()
print(cc)


