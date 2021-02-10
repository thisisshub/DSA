class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findPath(root, path, k):
    
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if (root.left != None and findPath(root.left, path, k)) or (
        root.right != None and findPath(root.right, path, k)
    ):
        return True

    path.pop()
    return False


def method1(root, n1, n2):

    path1 = []
    path2 = []

    if not findPath(root, path1, n1) or not findPath(root, path2, n2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


if __name__ == "__main__":
    
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(timeit(lambda: method1(root, 4, 5), number=10000))  
    
