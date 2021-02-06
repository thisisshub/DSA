INT_MAX = 2147483647


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):

    if not root:
        return newNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def floor(root, key):

    if not root:
        return INT_MAX

    if root.data == key:
        return root.data

    if root.data > key:
        return floor(root.left, key)

    floorValue = floor(root.right, key)
    return floorValue if (floorValue <= key) else root.data


if __name__ == "__main__":
    """
    from timeit import timeit

    root = None
    root = insert(root, 7)
    insert(root, 10)
    insert(root, 5)
    insert(root, 3)
    insert(root, 6)
    insert(root, 8)
    insert(root, 12)
    print(timeit(lambda: floor(root, 9), number=10000))  # 0.01083161299902713
    """