class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def method1(node):

    left_data = 0
    right_data = 0

    if node == None or (node.left == None and node.right == None):
        return 1
    else:

        if node.left != None:
            left_data = node.left.data

        if node.right != None:
            right_data = node.right.data

        if (
            (node.data == left_data + right_data)
            and method1(node.left)
            and method1(node.right)
        ):
            return 1
        else:
            return 0


if __name__ == "__main__":
    """
    from timeit import timeit

    root = newNode(10)
    root.left = newNode(8)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(2)
    print(timeit(lambda: method1(root), number=10000)) # 0.014636427004006691
    """
