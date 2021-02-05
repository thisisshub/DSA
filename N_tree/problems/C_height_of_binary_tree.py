class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def method1(node):
    if node is None:
        return -1

    else:

        lDepth = method1(node.left)
        rDepth = method1(node.right)

        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(timeit(lambda: (method1(root)), number=10000))
    """
