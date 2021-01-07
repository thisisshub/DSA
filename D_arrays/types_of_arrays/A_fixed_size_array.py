def method1():
    import array
    arr = array.array('i', (1, 2, 3, 4, 5))
    return arr

if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.0056163460003517685
    """