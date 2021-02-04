class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head):

        if head is None or head.next is None:
            return head

        rest = self.reverse(head.next)

        head.next.next = head
        head.next = None

        return rest

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = linkedListStr + str(temp.data) + " "
            temp = temp.next
        return linkedListStr

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp


if __name__ == "__main__":
    """
    from timeit import timeit
    linkedList = LinkedList()
    linkedList.push(1)
    linkedList.push(2)
    linkedList.push(3)
    linkedList.push(4)
    print(timeit(lambda: linkedList, number=10000)) # 0.00046981800005596597
    linkedList.head = linkedList.reverse(linkedList.head)
    print(timeit(lambda: linkedList, number=10000)) # 0.0004048120008519618
    """
