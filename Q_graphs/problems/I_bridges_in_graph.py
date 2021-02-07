from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridgeUtil(self, u, visited, parent, low, disc):

        visited[u] = True

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:

            if visited[v] == False:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    print(("%d %d" % (u, v)))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def bridge(self):

        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)


if __name__ == "__main__":
    """
    from timeit import  timeit

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)


    print("Bridges in first graph ")
    print(timeit(lambda: g1.bridge(), number=10000)) # 0.11896605800211546
    """
