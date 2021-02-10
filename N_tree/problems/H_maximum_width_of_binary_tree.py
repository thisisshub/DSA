class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getMaxWidth(root):
    maxWidth = 0
    h = height(root)

    for i in range(1, h + 1):
        width = getWidth(root, i)
        if width > maxWidth:
            maxWidth = width
    return maxWidth


def getWidth(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return getWidth(root.left, level - 1) + getWidth(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:

        lHeight = height(node.left)
        rHeight = height(node.right)

        return (lHeight + 1) if (lHeight > rHeight) else (rHeight + 1)


if __name__ == "__main__":
    
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    print(timeit(lambda: getMaxWidth(root), number=10000))  
    
