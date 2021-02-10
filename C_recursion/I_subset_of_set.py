def method1(n: list) -> list:
    x = len(n)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, n) if i & mask]


def method2(n: set) -> list:
    from itertools import combinations

    return [x for i in range(len(n) + 1) for x in combinations(n, i)]


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1([1, 2, 3, 4, 5, 6]), number=10000)) 
    print(timeit(lambda: method2({1, 2, 3, 4, 5, 6}), number=10000)) 
    
