class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0


def topview(root):

    if root == None:
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd

    q.append(root)

    while len(q):
        root = q[0]
        hd = root.hd

        if hd not in m:
            m[hd] = root.data
        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)

        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)

        q.pop(0)
    for i in sorted(m):
        print(m[i], end="")


if __name__ == "__main__":
    
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print(timeit(lambda: topview(root), number=10000))  
    
