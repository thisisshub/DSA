def method1(ll: list) -> list:
    def cycleSort(ll):
        writes = 0

        for cycleStart in range(0, len(ll) - 1):
            item = ll[cycleStart]
            pos = cycleStart

            for i in range(cycleStart + 1, len(ll)):
                if ll[i] < item:
                    pos += 1

            if pos == cycleStart:
                continue

            while item == ll[pos]:
                pos += 1
                ll[pos], item = item, ll[pos]
                writes += 1

            while pos != cycleStart:
                pos = cycleStart
                
                for i in range(cycleStart + 1, len(ll)):
                    if ll[i] < item:
                        pos += 1

            while item == ll[pos]:
                pos += 1
                ll[pos], item = item, ll[pos]
                writes += 1

        return writes

    return cycleSort(ll)


if __name__ == "__main__":
    """
    l = [1, 3, 4]
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) # 0.012405524001223966
    """
