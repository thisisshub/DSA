class Node:
    left = right = None

    def __init__(self, data):
        self.data = data


def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def insert(root, key):

    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    else:

        root.right = insert(root.right, key)

    return root


if __name__ == "__main__":
    """
    from timeit import timeit

    root = None
    keys = [15, 10, 20, 8, 12, 16, 25]

    for key in keys:
        root = insert(root, key)
    print(timeit(lambda: root, number=10000))  # 0.00042487999962759204
    """
