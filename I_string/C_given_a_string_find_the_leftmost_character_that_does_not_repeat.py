def method1(string: str) -> str:
    def character_count_array(string: str) -> int:
        count = [0] * 256
        for i in string:
            count[ord(i)] += 1
        return count

    def first_non_repeating(string: str) -> int:
        count = character_count_array(string)
        index = -1
        k = 0
        for i in string:
            if count[ord(i)] == 1:
                index = k
                break
            k += 1
        return index

    index = first_non_repeating(string)
    return string[index]


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1("thisisisastring"), number=10000))
    """
