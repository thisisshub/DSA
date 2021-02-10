def method1(arr1, arr2, n1, n2):
    hs = set()
    for i in range(0, n1):
        hs.add(arr1[i])
    for i in range(0, n2):
        hs.add(arr2[i])
    print("Union:")
    for i in hs:
        print(i, end=" ")
    print("\n")


if __name__ == "__main__":
    
    from timeit import timeit
    arr1 = [7, 1, 5, 2, 3, 6]
    arr2 = [3, 8, 6, 20, 7]
    n1 = len(arr1)
    n2 = len(arr2)
    print(timeit(lambda: method1(arr1, arr2, n1, n2), number=10000)) 
    
