from heapq import heappop, heappush, heapify


def print_array(arr: list):
    for elem in arr:
        print(elem, end=" ")


def sort_k(arr: list, n: int, k: int):
    heap = arr[: k + 1]

    heapify(heap)

    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1

    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1


if __name__ == "__main__":
    """
    from timeit import timeit

    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    n = len(arr)
    print(timeit(lambda: sort_k(arr, n, k), number=10000))  # 0.010045346996776061
    """