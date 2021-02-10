class newNode:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


def verticalSumUtil(root, hd, Map):

    if root == None:
        return

    verticalSumUtil(root.left, hd - 1, Map)

    if hd in Map.keys():
        Map[hd] = Map[hd] + root.data
    else:
        Map[hd] = root.data

    verticalSumUtil(root.right, hd + 1, Map)


def verticalSum(root):

    Map = {}

    verticalSumUtil(root, 0, Map)

    for i, j in Map.items():
        print(i, "=", j, end=", ")


if __name__ == "__main__":
    
    from timeit import timeit

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)

    print(timeit(lambda: verticalSum(root), number=10000))  
    
