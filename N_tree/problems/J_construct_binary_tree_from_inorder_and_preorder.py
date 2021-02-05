class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(inOrder, preOrder, inStrt, inEnd):

    if inStrt > inEnd:
        return None

    buildTree.preIndex = 0
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStrt == inEnd:
        return tNode

    inIndex = search(inOrder, inStrt, inEnd, tNode.data)

    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

    return tNode


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def method1(node):
    if node is None:
        return

    method1(node.left)

    print(node.data)

    method1(node.right)


if __name__ == "__main__":
    """
    from timeit import timeit

    inOrder = ["D", "B", "E", "A", "F", "C"]
    preOrder = ["A", "B", "D", "E", "C", "F"]

    buildTree.preIndex = 0
    root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

    print(timeit(lambda: method1(root), number=10000))  # 0.2564627779938746
    """
