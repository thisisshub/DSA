class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node("root", Node("left", Node("left.left")), Node("right"))
s = ""


def serialize(node, s=""):
    if not node:
        s += "
        return s
    s += str(node.val) + " "
    s = serialize(node.left, s=s)
    s = serialize(node.right, s=s)
    return s


i = 0


def deserialize(s):
    global i
    if s[i] == "
        if i < len(s) - 2:
            i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space + i
        node = Node(s[i:sp])
        i = sp + 1
        node.left = deserialize(s)
        node.right = deserialize(s)
        return node


if __name__ == "__main__":
    
    from timeit import timeit

    print(timeit(lambda: serialize(node), number=10000))  
    print(timeit(lambda: deserialize(serialize(node)), number=10000))  
    
