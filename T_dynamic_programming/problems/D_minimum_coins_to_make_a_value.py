import sys


def method1(coins, m, V):

    
    if V == 0:
        return 0

    
    res = sys.maxsize

    
    for i in range(0, m):
        if coins[i] <= V:
            sub_res = method1(coins, m, V - coins[i])

            
            
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    return res


if __name__ == "__main__":
    
    from timeit import timeit

    coins = [9, 6, 5, 1]
    m = len(coins)
    V = 11
    print(timeit(lambda: method1(coins, m, V), number=10000))  
    