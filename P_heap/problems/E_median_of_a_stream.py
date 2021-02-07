import heapq

maxh = []
minh = []
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in vals:

    if not maxh and not minh:
        heapq.heappush(maxh, -val)
        print(float(val))
    elif maxh:

        if val >= -maxh[0]:
            heapq.heappush(minh, val)
        else:
            heapq.heappush(maxh, -val)

        if len(maxh) == len(minh):
            print(float(-maxh[0] + minh[0]) / 2)
        elif len(maxh) == len(minh) + 1:
            print(float(-maxh[0]))
        elif len(minh) == len(maxh) + 1:
            print(float(minh[0]))

        elif len(minh) == len(maxh) + 2:
            heapq.heappush(maxh, -heapq.heappop(minh))
            print(float(-maxh[0] + minh[0]) / 2)
        elif len(maxh) == len(minh) + 2:
            heapq.heappush(minh, -heapq.heappop(maxh))
            print(float(-maxh[0] + minh[0]) / 2)

if __name__ == "__main__":
    """
    from timeit import timeit

    print(timeit((lambda: float(-maxh[0] + minh[0]) / 2), number=10000))  # 0.0013756349981122185
    """
