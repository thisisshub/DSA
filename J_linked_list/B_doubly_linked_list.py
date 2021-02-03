class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.data = data


if __name__ == "__main__":
    """
    from timeit import timeit
    DoublyLl = Node()
    print(timeit(lambda: DoublyLl, number=10000)) # 0.00042409200068505015
    """
