def method1(ll: list) -> list:
    def swap(i, j):
        ll[i], ll[j] = ll[j], ll[i]

    def heapify(end, i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max = i
        if l < end and ll[i] < ll[l]:
            max = l
        if r < end and ll[max] < ll[r]:
            max = r
        if max != i:
            swap(i, max)
            heapify(end, max)

    def heap_sort():
        end = len(ll)
        start = end // 2 - 1
        for i in range(start, -1, -1):
            heapify(end, i)
        for i in range(end - 1, 0, -1):
            swap(i, 0)
            heapify(i, 0)

    return heap_sort()


if __name__ == "__main__":
    
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) 
    
