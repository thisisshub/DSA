class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)


if __name__ == "__main__":
    """
    from timeit import timeit
    llist.head.next.next.next.next = llist.head
    if llist.detectLoop():
        print(timeit(lambda: llist.detectLoop(), number=10000)) # 0.005036081999605813
    else:
        print("No loop")
    """
