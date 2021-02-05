def method1():
    def is_operand(c):
        return c.isdigit()

    def evaluate(expression):

        stack = []

        for c in expression[::-1]:

            if is_operand(c):
                stack.append(int(c))

            else:
                o1 = stack.pop()
                o2 = stack.pop()

                if c == "+":
                    stack.append(o1 + o2)

                elif c == "-":
                    stack.append(o1 - o2)

                elif c == "*":
                    stack.append(o1 * o2)

                elif c == "/":
                    stack.append(o1 / o2)

        return stack.pop()

    test_expression = "+9*26"
    return evaluate(test_expression)


if __name__ == "__main__":
    """
    from timeit import timeit

    print(timeit(lambda: method1(), number=10000))  # 0.015567280002869666
    """
