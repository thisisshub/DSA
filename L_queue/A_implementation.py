def method1(queue: list) -> list:

    queue.append("a")
    queue.append("b")
    queue.append("c")

    print("Initial queue")
    print(queue)

    print("\nElements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print("\nQueue after removing elements")
    return queue


if __name__ == "__main__":
    
    from timeit import timeit

    print(timeit(lambda: method1([]), number=10000)) 
    
