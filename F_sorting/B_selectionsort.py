def method1(l: list) -> list:
    import sys

    for i in range(len(l)):
        minid = i
        for j in range(i + 1, len(l)):
            if l[minid] > l[j]:
                minid = j
        l[i], l[minid] = l[minid], l[i]
    return l


if __name__ == "__main__":
    
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    print(timeit(method1(l), number=10000)) 
    
