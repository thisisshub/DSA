import sys
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root


def findPairUtil(root, summ, unsorted_set):
    if root is None:
        return False
    if findPairUtil(root.left, summ, unsorted_set):
        return True
    if unsorted_set and (summ - root.data) in unsorted_set:
        print("Pair is Found ({},{})".format(summ - root.data, root.data))
        return True
    else:
        unsorted_set.add(root.data)

    return findPairUtil(root.right, summ, unsorted_set)


def findPair(root, summ):
    unsorted_set = set()
    if not findPairUtil(root, summ, unsorted_set):
        print("Pair do not exist!")


if __name__ == "__main__":
    """
    from timeit import timeit

    root = None
    root = insert(root, 15)
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 12)
    root = insert(root, 16)
    root = insert(root, 25)
    root = insert(root, 10)
    summ = 33
    print(timeit(lambda: findPair(root, summ), number=10000))  # 0.10178953700233251
    """
