bitsettable = [0] * 256
bitsettable[0] = 0

for i in range(256): bitsettable[i] = (i & 1) + bitsettable[i // 2]

def method1(n: int) -> int:
    return (bitsettable[n & 0xff] + 
            bitsettable[(n >> 8) & 0xff] +
            bitsettable[(n >> 16) & 0xff] +
            bitsettable[(n >> 24 & 0xff)])
        
if __name__ == '__main__':
    """
    from timeit import timeit
    print(timeit(lambda: method1(9), number=10000)) # 0.003812235000623332
    """