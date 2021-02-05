class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def findMax(root):

    if root == None:
        return float("-inf")

    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res


if __name__ == "__main__":
    """
    from timeit import timeit

    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)

    print(timeit(lambda: findMax(root)), number=10000)
    """
