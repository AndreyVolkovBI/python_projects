path = "files/4.txt"
graph = []
workTable = "*"
freeTable = "."
with open(path, 'r') as f:
    n = int(f.readline())  # размерность матрицы
    for i in range(n):
        graph.append(list(f.readline())[:-1])
    sitI, sitJ = map(int, f.readline().split())  # куда сел наш парень
    Adj = {}  # {vertex: [reachable vertices]}
    freeTables = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == freeTable:
                freeTables.append((i, j))


    def areNeighbours(x1, y1, x2, y2):
        # distance between two points formula
        return True if (x2 ** 2 - 2 * x2 * x1 + x1 ** 2) + (y2 ** 2 - 2 * y2 * y1 + y1 ** 2) == 1 else False

    for cell in freeTables:
        Adj[cell] = []
        x1, y1 = cell
        for i in range(len(freeTables)):
            x2, y2 = freeTables[i]
            if areNeighbours(x1, y1, x2, y2):
                Adj[cell].append((x2, y2))


    def bfs(s, Adj):
        parent = {s: None}
        frontier = [s]
        while frontier:
            next = []
            for u in frontier:
                if u in Adj:
                    for v in Adj[u]:
                        if v not in parent:
                            parent[v] = u
                            next.append(v)
            frontier = next
        return parent

    parent = bfs((sitI - 1, sitJ - 1), Adj)
    print(len(parent))
