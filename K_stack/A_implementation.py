
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


def method2():
    stack = []

    stack.append("a")
    stack.append("b")
    stack.append("c")

    print("Initial stack")
    print(stack)

    print("\nElements poped from stack:")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print("\nStack after elements are poped:")
    return stack


def method3():
    from collections import deque

    stack = deque()

    stack.append("a")
    stack.append("b")
    stack.append("c")

    print("Initial stack:")
    print(stack)

    print("\nElements poped from stack:")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print("\nStack after elements are poped:")
    return stack


if __name__ == "__main__":
    
    from timeit import timeit

    stack_ = Stack()
    for i in range(1, 11):
        stack_.push(i)
    print(timeit(lambda: f"Stack: {stack_}", number=10000)) 

    print(timeit(lambda: method2(), number=10000)) 
    print(timeit(lambda: method3(), number=10000)) 
    
