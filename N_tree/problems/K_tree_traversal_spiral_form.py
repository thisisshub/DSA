class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def method1(root):

    d = []

    d.append(root)

    direct = 0
    while len(d) != 0:
        size = len(d)

        while size:
            size -= 1

            if direct == 0:
                temp = d.pop()

                if temp.right:
                    d.insert(0, temp.right)

                if temp.left:
                    d.insert(0, temp.left)

                print(temp.data, end=" ")

            else:
                temp = d[0]
                d.pop(0)

                if temp.left:
                    d.append(temp.left)

                if temp.right:
                    d.append(temp.right)

                print(temp.data, end=" ")

        print()

        direct = 1 - direct


if __name__ == "__main__":
    
    from timeit import timeit

    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)

    print(timeit(lambda: method1(root), number=10000))  
    
