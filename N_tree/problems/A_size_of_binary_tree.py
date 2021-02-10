class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size(node):
    if node is None:
        return 0
    else:
        return size(node.left) + 1 + size(node.right)


if __name__ == "__main__":
    
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(timeit(lambda: size(root), number=10000))  
    
