class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0 for i in range(len(nums))]
        size = 0
        for x in nums:
            i = 0
            j = size
            while i != j:
                mid = i + (j - i) // 2
                if tails[mid] < x:
                    i = mid + 1
                else:
                    j = mid
                    tails[i] = x
                    size = max(i + 1, size)
        return size


if __name__ == "__main__":
    
    from timeit import timeit

    ob1 = Solution()
    print(
        timeit(lambda: ob1.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), number=10000)
    )  
    