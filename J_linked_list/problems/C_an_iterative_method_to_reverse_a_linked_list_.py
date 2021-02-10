class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev = None
        cur = self.head

        while cur:
            next_element = cur.next
            cur.next = prev
            prev = cur
            cur = next_element

        self.head = prev

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        cur = self.head
        l1 = []
        while cur:
            l1.append(cur.data)
            cur = cur.next
        return l1


if __name__ == "__main__":
    
    from timeit import timeit
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    print(timeit(lambda: llist.print_list(), number=10000)) 
    print(timeit(lambda: llist.reverse(), number=10000)) 
    print(timeit(lambda: llist.print_list(), number=10000)) 
    
