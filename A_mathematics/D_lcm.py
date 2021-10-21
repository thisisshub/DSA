def method1(n: int, m: int) -> int:
    '''This function computes LCM 
    calculated from GCD by Euclidean Algorithm.
    '''

    def gcd(n: int, m: int) -> int:
        '''This function computes GCD.'''

        while m:
            n, m = m, n % m
        return n

    return abs((n * m) // gcd(n, m))


def method2(n: int, m: int) -> int:
    '''This function computes LCM 
    calculated from GCD by inbuilt gcd() method.
    '''

    from math import gcd

    return abs(n * m) // gcd(n, m)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(2, 3), number=10000)) # 0.0052234140021028
    print(timeit(lambda: method2(2, 3), number=10000)) # 0.010972605999995722
    """
