class Node:
    def __init__(self, key):

        self.data = key
        self.hd = 1000000
        self.left = None
        self.right = None


def bottomView(root):

    if root == None:
        return

    hd = 0

    m = dict()

    q = []

    root.hd = hd

    q.append(root)

    while len(q) != 0:
        temp = q[0]

        q.pop(0)

        hd = temp.hd

        m[hd] = temp.data

        if temp.left != None:
            temp.left.hd = hd - 1
            q.append(temp.left)

        if temp.right != None:
            temp.right.hd = hd + 1
            q.append(temp.right)

    for i in sorted(m.keys()):
        print(m[i], end=" ")


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    print(timeit(lambda: bottomView(root), number=10000))  # 0.08178278699779185
    """
