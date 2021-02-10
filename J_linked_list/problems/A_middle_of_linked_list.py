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
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    def printMiddle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("The middle element is ", slow.data)


llist = LinkedList()

for i in range(5, 0, -1):
    llist.push(i)
    llist.printList()
    llist.printMiddle()

if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: llist.printMiddle(), number=10000)) 
    
