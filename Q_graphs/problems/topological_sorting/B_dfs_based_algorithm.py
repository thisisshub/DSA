graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == "__main__":
    
    from timeit import timeit

    print(timeit(lambda: dfs(visited, graph, "A"), number=10000)) 
    
