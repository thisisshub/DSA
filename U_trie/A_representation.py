_end = "_end_"


def method1(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root


if __name__ == "__main__":
    
    from timeit import timeit

    print(timeit(lambda: method1("foo", "bar", "bob", "cat")))  
    
