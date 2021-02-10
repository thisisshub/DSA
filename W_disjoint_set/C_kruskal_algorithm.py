class DisjointSet:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, N):

        # create `N` disjoint sets (one for each vertex)
        for i in range(N):
            self.parent[i] = i

    # Find the root of the set in which element `k` belongs
    def Find(self, k):

        # if `k` is root
        if self.parent[k] == k:
            return k

        # recur for the parent until we find the root
        return self.Find(self.parent[k])

    # Perform Union of two subsets
    def Union(self, a, b):

        # find the root of the sets in which elements
        # `x` and `y` belongs
        x = self.Find(a)
        y = self.Find(b)

        self.parent[x] = y


# Function to construct MST using Kruskal’s algorithm
def KruskalAlgo(edges, N):

    # stores the edges present in MST
    MST = []

    # Initialize `DisjointSet` class.
    # Create a singleton set for each element of the universe.
    ds = DisjointSet()
    ds.makeSet(N)

    index = 0

    # MST contains exactly `V-1` edges
    while len(MST) != N - 1:

        # consider the next edge with minimum weight from the graph
        (src, dest, weight) = edges[index]
        index = index + 1

        # find the root of the sets to which two endpoints
        # vertices of the next edge belongs
        x = ds.Find(src)
        y = ds.Find(dest)

        # if both endpoints have different parents, they belong to
        # different connected components and can be included in MST
        if x != y:
            MST.append((src, dest, weight))
            ds.Union(x, y)

    return MST


if __name__ == "__main__":
    """
    from timeit import timeit

    # `(u, v, w)` Triplet represent undirected edge from
    # vertex `u` to vertex `v` having weight `w`
    edges = [
        (0, 1, 7),
        (1, 2, 8),
        (0, 3, 5),
        (1, 3, 9),
        (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15),
        (3, 5, 6),
        (4, 5, 8),
        (4, 6, 9),
        (5, 6, 11),
    ]

    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])

    # total number of nodes in the graph
    N = 7

    # construct graph
    print(timeit(lambda: KruskalAlgo(edges, N), number=10000))  # 0.06291840798803605
    """
