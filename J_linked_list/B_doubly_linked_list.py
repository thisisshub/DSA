class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next  
        self.prev = prev  
        self.data = data


if __name__ == "__main__":
    
    from timeit import timeit
    DoublyLl = Node()
    print(timeit(lambda: DoublyLl, number=10000)) 
    
