def method1(myStr: str) -> bool:
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1("{[]{()}}"), number=10000)) # 0.013378982999711297
    """
