head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def segregateEvenOdd():
    global head
    end = head
    prev = None
    curr = head

    while end.next != None:
        end = end.next
    new_end = end

    while curr.data % 2 != 0 and curr != end:
        new_end.next = curr
        curr = curr.next
        new_end.next.next = None
        new_end = new_end.next

    if curr.data % 2 == 0:
        head = curr
        while curr != end:
            if curr.data % 2 == 0:
                prev = curr
                curr = curr.next

            else:
                prev.next = curr.next
                curr.next = None
                new_end.next = curr
                new_end = curr
                curr = prev.next

    else:
        prev = curr

    if new_end != end and end.data % 2 != 0:
        prev.next = end.next
        end.next = None
        new_end.next = end


def push(new_data):
    global head
    new_node = Node(new_data)
    new_node.next = head
    head = new_node


def printList():
    global head
    temp = head
    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next
    print(" ")


if __name__ == "__main__":
    """
    from timeit import timeit
    push(11)
    push(10)
    push(8)
    push(6)
    push(4)
    push(2)
    push(0)
    segregateEvenOdd()
    print(timeit(lambda: printList(), number=10000)) # 0.10623525099981634
    """
