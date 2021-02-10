class ListNode:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


def print_list(head):
    ptr = head
    print("[", end="")
    while ptr:
        print(ptr.val, end=", ")
        ptr = ptr.next
    print("]")


class Heap:
    def __init__(self):
        self.arr = []

    def print_heap(self):
        res = " "
        for i in self.arr:
            res += str(i.val) + " "
        print(res)

    def getVal(self, i):
        return self.arr[i].val

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.arr.append(value)
        n = len(self.arr) - 1
        i = n
        while i != 0 and self.arr[i].val < self.arr[self.parent(i)].val:
            self.arr[i], self.arr[self.parent(i)] = (
                self.arr[self.parent(i)],
                self.arr[i],
            )
            i = self.parent(i)

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i
        n = len(self.arr)
        if left < n and self.getVal(left) < self.getVal(smallest):
            smallest = left
        if right < n and self.getVal(right) < self.getVal(smallest):
            smallest = right
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.heapify(smallest)

    def extractMin(self):
        n = len(self.arr)
        if n == 0:
            return "
        if n == 1:
            temp = self.arr[0]
            self.arr.pop()
            return temp
        root = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.heapify(0)
        return root


class Solution(object):
    def mergeKLists(self, lists):
        heap = Heap()
        for i in lists:
            if i:
                heap.insert(i)
        res = None
        res_next = None
        while True:
            temp = heap.extractMin()
            if temp == "
                return res
            if not res:
                res = temp
                res_next = temp
                temp = temp.next
                if temp:
                    heap.insert(temp)
                res.next = None
        else:
            res_next.next = temp
            temp = temp.next
            res_next = res_next.next
            if temp:
                heap.insert(temp)
            res_next.next = None


if __name__ == "__main__":
    
    from timeit import timeit

    ob = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lls = []
    for ll in lists:
        l = make_list(ll)
        lls.append(l)

    print(timeit(lambda: print_list(ob.mergeKLists(lls)), number=10000)) 
    
