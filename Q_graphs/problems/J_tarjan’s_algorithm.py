from collections import defaultdict


class Graph:
    def __init__(self, vertices):

        self.V = vertices

        self.graph = defaultdict(list)

        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def SCCUtil(self, u, low, disc, stackMember, st):

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        for v in self.graph[u]:

            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st)

                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:

                low[u] = min(low[u], disc[v])

        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                stackMember[w] = False

            print("")

    def SCC(self):

        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)


if __name__ == "__main__":
    """
    from timeit import timeit

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    print("SSC in first graph ")
    print(timeit(lambda: g1.SCC(), number=10000))  # 0.18323329299892066
    """
