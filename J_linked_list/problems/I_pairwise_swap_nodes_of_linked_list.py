class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pairwiseSwap(self):
        temp = self.head

        if temp is None:
            return

        while temp is not None and temp.next is not None:
            if temp.data == temp.next.data:
                temp = temp.next.next
            else:
                temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    """
    from timeit import timeit
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.pairwiseSwap()
    print(timeit(lambda: llist.printList(), number=10000))  # 0.27164168400122435
    """
