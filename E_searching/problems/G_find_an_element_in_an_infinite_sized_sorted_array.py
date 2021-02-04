def binary_search(ll: list,l: int,r:int,x: int) -> int: 
    if r >= l: 
        mid = int(l+(r-l)/2)
        if ll[mid] == x: 
            return mid 
        if ll[mid] > x: 
            return binary_search(ll,l,mid-1,x) 
        return binary_search(ll,mid+1,r,x) 
    return -1


def method1(a, key): 
    l, h, val = 0, 1, ll[0] 
    while val < key: 
        l = h        
        h = 2*h       
        val = ll[h]
    return binary_search(a, l, h, key) 
  

if __name__ == "__main__":
    """
    from timeit import timeit
    ll = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] 
    print(timeit(lambda: method1(ll,10), number=10000)) # 0.007889933999649656
    """