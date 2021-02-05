def method1():
    def infix_2_postfix(Infix):
        Stack = []
        Postfix = []
        priority = {
            "^": 3,
            "*": 2,
            "/": 2,
            "%": 2,
            "+": 1,
            "-": 1,
        }
        print_width = len(Infix) if (len(Infix) > 7) else 7

        print(
            "Symbol".center(8),
            "Stack".center(print_width),
            "Postfix".center(print_width),
            sep=" | ",
        )
        print("-" * (print_width * 3 + 7))

        for x in Infix:
            if x.isalpha() or x.isdigit():
                Postfix.append(x)
            elif x == "(":
                Stack.append(x)
            elif x == ")":
                while Stack[-1] != "(":
                    Postfix.append(Stack.pop())
                Stack.pop()
            else:
                if len(Stack) == 0:
                    Stack.append(x)
                else:
                    while len(Stack) > 0 and priority[x] <= priority[Stack[-1]]:
                        Postfix.append(Stack.pop())
                    Stack.append(x)

            print(
                x.center(8),
                ("".join(Stack)).ljust(print_width),
                ("".join(Postfix)).ljust(print_width),
                sep=" | ",
            )

        while len(Stack) > 0:
            Postfix.append(Stack.pop())
            print(
                " ".center(8),
                ("".join(Stack)).ljust(print_width),
                ("".join(Postfix)).ljust(print_width),
                sep=" | ",
            )

        return "".join(Postfix)

    def infix_2_prefix(Infix):
        Infix = list(Infix[::-1])

        for i in range(len(Infix)):
            if Infix[i] == "(":
                Infix[i] = ")"
            elif Infix[i] == ")":
                Infix[i] = "("

        return (infix_2_postfix("".join(Infix)))[::-1]

    return infix_2_prefix


if __name__ == "__main__":
    """
    from timeit import timeit

    print(timeit(lambda: method1(), number=10000)) # 0.002016692997131031
    """
