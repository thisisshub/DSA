class Node:
    def __init__(self, data):

        self.key = data
        self.left = None
        self.right = None


def correctBstUtil(root, first, middle, last, prev):

    if root:

        correctBstUtil(root.left, first, middle, last, prev)

        if prev[0] and root.key < prev[0].key:
            if not first[0]:
                first[0] = prev[0]
                middle[0] = root
            else:

                last[0] = root

        prev[0] = root

        correctBstUtil(root.right, first, middle, last, prev)


def correctBst(root):

    first = [None]
    middle = [None]
    last = [None]
    prev = [None]

    correctBstUtil(root, first, middle, last, prev)

    if first[0] and last[0]:

        first[0].key, last[0].key = (last[0].key, first[0].key)

    elif first[0] and middle[0]:

        first[0].key, middle[0].key = (middle[0].key, first[0].key)


def PrintInorder(root):

    if root:
        PrintInorder(root.left)
        print(root.key, end=" ")
        PrintInorder(root.right)

    else:
        return


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(6)
    root.left = Node(10)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(7)
    root.right.right = Node(12)

    print(timeit(lambda: correctBst(root), number=10000))  # 0.018424429996230174
    """
