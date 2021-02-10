def construct_segment_tree(segtree, a, n):

    
    
    for i in range(n):
        segtree[n + i] = a[i]

    
    
    for i in range(n - 1, 0, -1):
        segtree[i] = min(segtree[2 * i], segtree[2 * i + 1])


def range_query(segtree, left, right, n):
    left += n
    right += n

    
		will move towards right and left respectively 
		and with every each next higher level and 
		compute the minimum at each height change 
		the index to leaf node first 

    mi = 1e9  
    while left < right:
        if left & 1:  
            mi = min(mi, segtree[left])
            left = left + 1
        if right & 1:  
            right -= 1
            mi = min(mi, segtree[right])

        
        left = left // 2
        right = right // 2
    return mi


def update(segtree, pos, value, n):

    
    pos += n

    
    
    segtree[pos] = value
    while pos > 1:

        
        pos >>= 1

        
        
        segtree[pos] = min(segtree[2 * pos], segtree[2 * pos + 1])



a = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
n = len(a)



segtree = [0 for i in range(2 * n)]
construct_segment_tree(segtree, a, n)
left = 0
right = 5  
print(
    "Minimum in range",
    left,
    "to",
    right,
    "is",
    range_query(segtree, left, right + 1, n),
)


index = 3
value = 1

if __name__ == "__main__":
    
    from timeit import timeit

    update(segtree, index, value, n)  
    left = 2
    right = 6  
    print(
        timeit(lambda: range_query(segtree, left, right + 1, n), number=10000)
    )  
    
