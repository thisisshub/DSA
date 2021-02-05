class Node(object):
    
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def BTToDLLUtil(root):

    if root is None:
        return root

    if root.left:

        left = BTToDLLUtil(root.left)

        while left.right:
            left = left.right

        left.right = root

        root.left = left

    if root.right:

        right = BTToDLLUtil(root.right)

        while right.left:
            right = right.left

        right.left = root

        root.right = right

    return root


def BTToDLL(root):
    if root is None:
        return root

    root = BTToDLLUtil(root)

    while root.left:
        root = root.left

    return root


def method1(head):

    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    head = BTToDLL(root)
    print(timeit(lambda: method1(head), number=10000))  # 0.05323586200393038
    """
