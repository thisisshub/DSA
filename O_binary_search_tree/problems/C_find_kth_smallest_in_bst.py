class Node:
    def __init__(self, key):

        self.data = key
        self.left = None
        self.right = None


def insert(root, x):

    if root == None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    return root


def kthSmallest(root, k):

    if root == None:
        return None

    left = kthSmallest(root.left, k)

    if left != None:
        return left

    k -= 1
    if k == 0:
        return root

    return kthSmallest(root.right, k)


def printKthSmallest(root):

    res = kthSmallest(root, k)

    if res == None:
        print("There are less than k nodes in the BST")
    else:
        print("K-th Smallest Element is ", res.data)


if __name__ == "__main__":
    from timeit import timeit

    root = None
    keys = [20, 8, 22, 4, 12, 10, 14]

    for x in keys:
        root = insert(root, x)

    k = 3

    print(timeit(lambda: printKthSmallest(root), number=10000))  
