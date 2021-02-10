import sys


def method1(p, i, j):

    if i == j:
        return 0

    _min = sys.maxsize

    
    
    
    
    
    for k in range(i, j):

        count = (
            method1(p, i, k)
            + method1(p, k + 1, j)
            + p[i - 1] * p[k] * p[j]
        )

        if count < _min:
            _min = count

    return _min


if __name__ == "__main__":
    
    from timeit import timeit

    arr = [1, 2, 3, 4, 3]
    n = len(arr)

    print(
        timeit(lambda: method1(arr, 1, n - 1), number=10000)
    )  
    