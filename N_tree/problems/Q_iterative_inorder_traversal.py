class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root):

    current = root
    stack = []

    while True:

        if current is not None:

            stack.append(current)

            current = current.left

        elif stack:
            current = stack.pop()
            print(current.data, end=" ")

            current = current.right

        else:
            break

    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(timeit(lambda: inOrder(root), number=10000))  # 0.15916127999980745
    """