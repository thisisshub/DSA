def method1(string: str) -> int:
    def fact(n: int) -> int:
        return 1 if n == 1 or n == 0 else n * fact(n - 1)

    def find_smaller_in_right(st, low, high):
        count_right = 0
        i = low + 1
        while i <= high:
            if st[i] < st[low]:
                count_right = count_right + 1
            i += 1
        return count_right

    def find_rank(st):
        mul = fact(len(st))
        rank = 1
        i = 0
        while i < len(st):
            mul = mul / (len(st) - i)
            count_right = find_smaller_in_right(st, i, len(st) - 1)
            rank += count_right * mul
            i += 1
        return rank

    st = "thisisastring"
    return find_rank(st)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1("thisisastring"), number=10000)) # 0.10805942400020285
    """
