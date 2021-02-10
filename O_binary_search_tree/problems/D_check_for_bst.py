INT_MAX = 4294967296
INT_MIN = -4294967296


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)


def isBSTUtil(node, mini, maxi):

    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return isBSTUtil(node.left, mini, node.data - 1) and isBSTUtil(
        node.right, node.data + 1, maxi
    )


if __name__ == "__main__":
    
    from timeit import timeit

    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    print(timeit(lambda: isBST(root), number=10000))  
    
