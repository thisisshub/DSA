def construct_segment_tree(segtree, a, n):

    # assign values to leaves of
    # the segment tree
    for i in range(n):
        segtree[n + i] = a[i]

    # assign values to remaining nodes
    # to compute minimum in a given range
    for i in range(n - 1, 0, -1):
        segtree[i] = min(segtree[2 * i], segtree[2 * i + 1])


def range_query(segtree, left, right, n):
    left += n
    right += n

    """ Basically the left and right indices 
		will move towards right and left respectively 
		and with every each next higher level and 
		compute the minimum at each height change 
		the index to leaf node first """

    mi = 1e9  # initialize minimum to a very high value
    while left < right:
        if left & 1:  # if left index in odd
            mi = min(mi, segtree[left])
            left = left + 1
        if right & 1:  # if right index in odd
            right -= 1
            mi = min(mi, segtree[right])

        # move to the next higher level
        left = left // 2
        right = right // 2
    return mi


def update(segtree, pos, value, n):

    # change the index to leaf node first
    pos += n

    # update the value at the leaf node
    # at the exact index
    segtree[pos] = value
    while pos > 1:

        # move up one level at a time in the tree
        pos >>= 1

        # update the values in the nodes
        # in the next higher level
        segtree[pos] = min(segtree[2 * pos], segtree[2 * pos + 1])



a = [2, 6, 10, 4, 7, 28, 9, 11, 6, 33]
n = len(a)

# Construct the segment tree by assigning
# the values to the internal nodes
segtree = [0 for i in range(2 * n)]
construct_segment_tree(segtree, a, n)
left = 0
right = 5  # compute minimum in the range left to right
print(
    "Minimum in range",
    left,
    "to",
    right,
    "is",
    range_query(segtree, left, right + 1, n),
)

# update the value of index 3 to 1
index = 3
value = 1

if __name__ == "__main__":
    """
    from timeit import timeit

    update(segtree, index, value, n)  # point update
    left = 2
    right = 6  # compute minimum in the range left to right
    print(
        timeit(lambda: range_query(segtree, left, right + 1, n), number=10000)
    )  # 0.008780983000178821
    """
