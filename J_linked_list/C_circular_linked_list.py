class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    """
    from timeit import timeit
    clist = CircularLinkedList()
    print(timeit(lambda: clist, number=10000)) # 0.0003614770000126555
    """
