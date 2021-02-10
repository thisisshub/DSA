def method1():
    def createStack():
        stack = []
        return stack

    def isEmpty(stack):
        return len(stack) == 0

    def push(stack, x):
        stack.append(x)

    def pop(stack):
        if isEmpty(stack):
            print("Error : stack underflow")
        else:
            return stack.pop()

    def print_nge(arr):
        s = createStack()
        element = 0
        next = 0

        push(s, arr[0])

        for i in range(1, len(arr), 1):
            next = arr[i]

            if isEmpty(s) == False:
                element = pop(s)
                while element < next:
                    print(str(element) + " -- " + str(next))
                    if isEmpty(s) == True:
                        break
                    element = pop(s)

                if element > next:
                    push(s, element)

            push(s, next)
        while isEmpty(s) == False:
            element = pop(s)
            next = -1
            print(str(element) + " -- " + str(next))

    return print_nge


def method2(arr):
    for i in range(0, len(arr), 1):
        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break

        return str(arr[i]) + " -- " + str(next)


if __name__ == "__main__":
    
    from timeit import timeit

    arr = [11, 13, 21, 3]
    print(timeit(lambda: method1(), number=10000))  
    print(timeit(lambda: method2(arr), number=10000))  
    
