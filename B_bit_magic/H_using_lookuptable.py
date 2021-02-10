bitsettable = [0] * 256
bitsettable[0] = 0

for i in range(256):
    bitsettable[i] = (i & 1) + bitsettable[i // 2]


def method1(n: int) -> int:
    return (
        bitsettable[n & 0xFF]
        + bitsettable[(n >> 8) & 0xFF]
        + bitsettable[(n >> 16) & 0xFF]
        + bitsettable[(n >> 24 & 0xFF)]
    )


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(9), number=10000)) 
    
