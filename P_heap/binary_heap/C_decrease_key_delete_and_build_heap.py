import math


class FibonacciTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1


class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert(self, key):
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if self.least is None or key < self.least.key:
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self):
        if self.least is None:
            return None
        return self.least.key

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key

    def consolidate(self):
        aux = (floor_log2(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.key < self.least.key:
                    self.least = k


def floor_log2(x):
    return math.frexp(x)[1] - 1


if __name__ == "__main__":
    """
    from timeit import timeit

    fheap = FibonacciHeap()

    fheap.insert(11)
    fheap.insert(10)
    fheap.insert(39)
    fheap.insert(26)
    fheap.insert(24)

    print(timeit(lambda: fheap.get_min(), number=10000))  # 0.0015727249992778525

    print(timeit(lambda: fheap.extract_min(), number=10000))  # 0.001127119001466781
    """
