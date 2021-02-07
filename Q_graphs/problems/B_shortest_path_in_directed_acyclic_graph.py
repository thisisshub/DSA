from collections import defaultdict


class Graph:
    def __init__(self, vertices):

        self.V = vertices

        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def topologicalSortUtil(self, v, visited, stack):

        visited[v] = True

        if v in self.graph.keys():
            for node, weight in self.graph[v]:
                weight = weight  # unused variable
                if visited[node] == False:
                    self.topologicalSortUtil(node, visited, stack)

        stack.append(v)

    def shortestPath(self, s):

        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(s, visited, stack)

        dist = [float("Inf")] * (self.V)
        dist[s] = 0

        while stack:

            i = stack.pop()

            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight

        for i in range(self.V):
            print("%d" % dist[i]) if dist[i] != float("Inf") else "Inf",


if __name__ == "__main__":
    """
    from timeit import timeit

    g = Graph(6)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 3, 6)
    g.addEdge(1, 2, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 3, 7)
    g.addEdge(3, 4, -1)
    g.addEdge(4, 5, -2)

    s = 1

    print(timeit(lambda: g.shortestPath(s), number=10000))  # 0.22385385600136942
    """
