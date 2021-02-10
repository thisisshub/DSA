class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def newNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    return new_node


def insertEnd(head, data):

    if head == None:
        return newNode(data)

    else:
        head.next = insertEnd(head.next, data)
    return head


def traverse(head):
    if head == None:
        return

    print(head.data, end=" ")
    traverse(head.next)


if __name__ == "__main__":
    
    from timeit import timeit
    head = None
    head = insertEnd(head, 6)
    head = insertEnd(head, 8)
    head = insertEnd(head, 10)
    head = insertEnd(head, 12)
    head = insertEnd(head, 14)
    print(timeit(lambda: traverse(head), number=10000)) 
    
