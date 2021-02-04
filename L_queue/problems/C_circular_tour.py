def method1():
    class PetrolPump:
        def __init__(self, petrol, distance):
            self.petrol = petrol
            self.distance = distance

    def printTour(arr):

        n = len(arr)

        start = 0
        end = 1

        curr_petrol = arr[start].petrol - arr[start].distance

        while end != start or curr_petrol < 0:

            while curr_petrol < 0 and start != end:

                curr_petrol -= arr[start].petrol - arr[start].distance
                start = (start + 1) % n

                if start == 0:
                    return -1

            curr_petrol += arr[end].petrol - arr[end].distance

            end = (end + 1) % n

        return start

    arr = [PetrolPump(6, 4), PetrolPump(3, 6), PetrolPump(7, 3)]
    start = printTour(arr)

    return ("No solution" if start == -1 else "start =", start)


if __name__ == "__main__":
    """
    from timeit import timeit
    print(timeit(lambda: method1(), number=10000)) # 0.07590579400130082
    """
