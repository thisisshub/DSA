def method1(ll: list, n: int) -> int:
    count = 0
    result = 0
    for i in range(0, n):
        if ll[i] == 0:
            count = 0
        else:
            count += 1
            result = max(result, count)

    return result


ll = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
n = len(ll)

if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(ll, n), number=10000)) 
    
