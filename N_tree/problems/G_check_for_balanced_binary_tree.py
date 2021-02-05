class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):

    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalanced(root):

    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

    if (
        (abs(lh - rh) <= 1)
        and isBalanced(root.left) is True
        and isBalanced(root.right) is True
    ):
        return True

    return False


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    print(timeit(lambda: isBalanced(root), number=10000))  # 0.01500733800639864
    """
