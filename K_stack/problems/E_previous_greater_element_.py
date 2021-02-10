def method1(arr, n):
    import math as mt

    s = list()
    s.append(arr[0])

    print("-1, ", end="")

    for i in range(1, n):

        while len(s) > 0 and s[-1] < arr[i]:
            s.pop()

        if len(s) == 0:
            print("-1, ", end="")
        else:
            print(s[-1], ", ", end="")

        s.append(arr[i])


def method2(arr, n):

    print("-1", end=", ")

    for i in range(1, n):
        flag = 0

        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                print(arr[j], end=", ")
                flag = 1
                break

        if j == 0 and flag == 0:
            print("-1", end=", ")


if __name__ == "__main__":
    
    from timeit import timeit

    arr = [10, 4, 2, 20, 40, 12, 30]
    n = len(arr)
    print(timeit(lambda: method1(arr, n), number=10000)) 
    print(timeit(lambda: method2(arr, n), number=10000)) 
    
