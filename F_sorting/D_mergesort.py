def method1(ll: list) -> list:
    def merge(left: list, right: list) -> list:
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def mergesort(list):
        if len(list) < 2:
            return list
        middle = len(list) / 2
        left = mergesort(list[:middle])
        right = mergesort(list[middle:])
        return merge(left, right)


if __name__ == "__main__":
    """
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) # 0.009614205999241676
    """
