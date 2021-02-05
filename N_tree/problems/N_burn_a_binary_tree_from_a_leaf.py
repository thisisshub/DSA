class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def _recurse(node, start):
    if node is None:
        return (None, 0)
    else:
        max_left, dist_left = _recurse(node.left, start)
        max_right, dist_right = _recurse(node.right, start)

        if node == start:
            return (0, 0)

        elif max_right is not None or max_left is not None:
            return (
                dist_right + dist_left + 1,
                (dist_left if max_right is None else dist_right) + 1,
            )

        else:
            return (None, max(dist_left, dist_right) + 1)


def time_to_burn(root, start):
    return _recurse(root, start)[0]


if __name__ == "__main__":
    """
    from timeit import timeit

    root = Node(1)
    root.left = Node(1)
    root.right = Node(1)
    root.left.left = Node(1)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.left.right.right = Node(1)
    root.right.right = Node(1)
    root.right.right.right = Node(1)
    root.right.right.right.right = Node(1)

    print(timeit(lambda: time_to_burn(root, root.left.right.right), number=10000))  # 0.026541252998868003
    """