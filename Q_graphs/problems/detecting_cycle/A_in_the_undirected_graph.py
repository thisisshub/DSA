from collections import defaultdict


class Graph:
    def __init__(self, vertices):

        self.V = vertices

        self.graph = defaultdict(list)

    def addEdge(self, v, w):

        self.graph[v].append(w)

        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:

            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v):
                    return True

            elif parent != i:
                return True

        return False

    def isCyclic(self):

        visited = [False] * (self.V)

        for i in range(self.V):

            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False


if __name__ == "__main__":
    """
    from timeit import timeit

    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    g1 = Graph(3)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)

    print(timeit(lambda: g1.isCyclic(), number=10000))  # 0.01144661000216729
    """
