def method1(arr):
    incl = 0
    excl = 0

    for i in arr:

        
        
        new_excl = excl if excl > incl else incl

        
        incl = excl + i
        excl = new_excl

    
    return excl if excl > incl else incl


if __name__ == "__main__":
    
    from timeit import timeit

    arr = [5, 5, 10, 100, 10, 5]
    print(timeit(lambda: method1(arr), number=10000))  
    