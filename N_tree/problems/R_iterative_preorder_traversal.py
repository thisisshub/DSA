class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterativePreorder(root):

    if root is None:
        return

    nodeStack = []
    nodeStack.append(root)

    while len(nodeStack) > 0:

        node = nodeStack.pop()
        print(node.data)

        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    print(timeit(lambda: iterativePreorder(root), number=10000)) # 0.2520280839999032
    """
