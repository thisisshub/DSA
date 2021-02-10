class DisjointSet:
    parent = {}

    
    def makeSet(self, N):

        
        for i in range(N):
            self.parent[i] = i

    
    def Find(self, k):

        
        if self.parent[k] == k:
            return k

        
        return self.Find(self.parent[k])

    
    def Union(self, a, b):

        
        
        x = self.Find(a)
        y = self.Find(b)

        self.parent[x] = y



def KruskalAlgo(edges, N):

    
    MST = []

    
    
    ds = DisjointSet()
    ds.makeSet(N)

    index = 0

    
    while len(MST) != N - 1:

        
        (src, dest, weight) = edges[index]
        index = index + 1

        
        
        x = ds.Find(src)
        y = ds.Find(dest)

        
        
        if x != y:
            MST.append((src, dest, weight))
            ds.Union(x, y)

    return MST


if __name__ == "__main__":
    
    from timeit import timeit

    
    
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

    
    edges.sort(key=lambda x: x[2])

    
    N = 7

    
    print(timeit(lambda: KruskalAlgo(edges, N), number=10000))  
    
