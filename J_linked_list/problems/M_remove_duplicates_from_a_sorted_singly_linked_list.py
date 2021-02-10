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

    def deleteNode(self, key):

        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head


if __name__ == "__main__":
    
    from timeit import timeit

    llist = LinkedList()
    llist.push(20)
    llist.push(13)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(11)

    print(timeit(lambda: llist.removeDuplicates(), number=10000)) 
    
