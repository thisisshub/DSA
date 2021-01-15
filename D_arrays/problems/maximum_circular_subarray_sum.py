def method1():

    from sys import maxsize

    def maxsubarraysum(a, size):
        max_so_far = -maxsize - 1
        max_ending_here = 0

        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

    def maxCircularSum(a):

        n = len(a)
        max_kadane = maxsubarraysum(a, size)
        max_wrap = 0
        for i in range(0, n):
            max_wrap += a[i]
            a[i] = -a[i]
        max_wrap = max_wrap + maxsubarraysum(a, size)

        if max_wrap > max_kadane:
            return max_wrap
        else:
            return max_kadane
        return maxsubarraysum(a, size)

    a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
    size = len(a)

    return maxCircularSum(a)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.04304332999890903
    """
