import heapq


class Solution(object):
    def find_Kth_Largest(self, nums, k):

        h = []
        for e in nums:
            heapq.heappush(h, (-e, e))
        for i in range(k):
            w, e = heapq.heappop(h)
            w = w
            if i == k - 1:
                return e


if __name__ == "__main__":
    
    from timeit import timeit

    arr_nums = [12, 14, 9, 50, 61, 41]
    s = Solution()
    result = s.find_Kth_Largest(arr_nums, 3)
    print(timeit(lambda: result, number=10000))  
    
