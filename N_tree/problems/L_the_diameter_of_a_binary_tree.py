class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(node):

    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))


def method1(root):

    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = method1(root.left)
    rdiameter = method1(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(timeit(lambda: method1(root), number=10000))  # 0.037249127999530174
    """
