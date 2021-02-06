class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def ceil(root, inp):

    if root == None:
        return -1

    if root.key == inp:
        return root.key

    if root.key < inp:
        return ceil(root.right, inp)

    val = ceil(root.left, inp)
    return val if val >= inp else root.key


if __name__ == "__main__":
    """
    from timeit import timeit
    root = Node(8)

    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(timeit(lambda: ceil(root, 9), number=10000))  # 0.005088308003905695
    """
