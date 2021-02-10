from queue import Queue


def method1():
    def Print(queue):
        while not queue.empty():
            print(queue.queue[0], end=", ")
            queue.get()

    def reversequeue(queue):
        Stack = []
        while not queue.empty():
            Stack.append(queue.queue[0])
            queue.get()
        while len(Stack) != 0:
            queue.put(Stack[-1])
            Stack.pop()
    
    queue = Queue()
    reversequeue(queue)
    return Print


if __name__ == "__main__":
    
    from timeit import timeit

    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    queue.put(5)
    queue.put(6)
    queue.put(7)
    queue.put(8)
    queue.put(9)
    queue.put(10)
    print(timeit(lambda: method1(), number=10000))
    
