def method1():
    def maxDiff(ll: list) -> int:
        vmin = ll[0]
        dmax = 0
        for i in range(len(ll)):
            if ll[i] < vmin:
                vmin = ll[i]
            elif ll[i] - vmin > dmax:
                dmax = ll[i] - vmin
        return dmax

    ll = [i for i in range(5)]
    return maxDiff(ll)


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) 
    
