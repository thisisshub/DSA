from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  

    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    
    
    def isCyclic(self):

        
        
        parent = [-1] * (self.V)

        
        
        
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


if __name__ == "__main__":
    
    from timeit import timeit

    
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    print(timeit(lambda: g.find_parent, number=10000))  
    print(timeit(lambda: g.union, number=10000))  
    
